import subprocess
import smtplib

def machine_is_known(mac):
  return mac in known_machines

def name_for_mac(mac):
  for m in all_machines:
    if m[1] == mac:
      return m[2]
  return ""

def ip_for_mac(mac):
  for m in all_machines:
    if m[1] == mac:
      return m[0]
  return ""

x = subprocess.check_output(["arp-scan","--interface=eth0", "--localnet"])
arr = x.strip().split('\n')

arr.pop()
arr.pop()
arr.pop()
arr = arr[2:]

all_machines = []

for line in arr:
  all_machines.append(line.split('\t')) #ip\tmac address\tname

known_machines_file = open('/home/pi/network-alert/known_machines', 'a+')
known_machines = known_machines_file.read().strip().split('\n')

message = ""

print "matches"
for c in all_machines:
  mac = c[1]
  if not machine_is_known(mac):
    message = message + "\n MAC: " + mac + ", NAME: " + name_for_mac(mac) + ", IP: " + ip_for_mac(mac)
    known_machines_file.write(mac + '\n')


if len(message) > 0:
  smtp = smtplib.SMTP('localhost')
  smtp.sendmail('network-alert@michael.mccanns.org', ['mccannmike11@gmail.com'], str(message) )
  smtp.quit()


known_machines_file.close()



 


  

