import smtplib
import ConfigParser
from scanner import Scanner

config = ConfigParser.RawConfigParser()
config.read('config.cfg')

KNOWN_MACHINES_FILE = config.get('config', 'known_machines_file')
INTERFACE = config.get('config', 'interface')
SMTP_SERVER = config.get('config', 'smtp_server')
ALERTING_USER = config.get('config', 'alerting_user')
USERS_TO_ALERT = config.get('config', 'users_to_alert').split(',')


s = Scanner(KNOWN_MACHINES_FILE, INTERFACE)
alert = ""

for m in s.unknown_machines:
  alert = alert + "\n MAC: " + m['mac'] + " Name: " + m['name'] + " IP: "+ m['ip']
  s.add_to_known_machines(m['mac'])

if len(alert) > 0:
  smtp = smtplib.SMTP(SMTP_SERVER)
  smtp.sendmail(ALERTING_USER, USERS_TO_ALERT, str(alert))
  smtp.quit()
