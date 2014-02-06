import subprocess

class Scanner(object):

    def __init__(self, interface):
        self.interface = interface

    def scan(self):
        self.devices = self.parse_devices(self.run_subprocess())

    def parse_devices(self, process_output):
        arr = process_output.strip().split('\n')
        arr = arr[2:len(arr) - 3]
        all_devices = []
        for line in arr: #ip\tmac address\tname
            all_devices.append(self.device_array_to_hash(line.split('\t')))
        return all_devices

    def run_subprocess(self):
        return subprocess.check_output(["arp-scan","--interface=" + self.interface, "--localnet"])

    def device_array_to_hash(self, array):
        return dict(zip(['ip', 'mac', 'name'], array))
