import subprocess

class Scanner(object):
    def __init__(self, file_name, interface, path):
        self.file_name = file_name
        self.interface = interface

    def scan(self):
        self.known_machines = self.read_known_machines()
        self.all_machines = self.scan_all_machines()
        self.unknown_machines = self.filter_unknown_machines()

    def add_to_known_machines(self, mac):
        file = open(self.file_name, 'a+')
        file.write(mac + "\n")
        file.close()

    def filter_unknown_machines(self):
        return [m for m in self.all_machines if not self.machine_is_known(m['mac'])]


    def read_known_machines(self):
        known_machines_file = open(self.file_name, 'a+')
        known = known_machines_file.read().strip().split('\n')
        known_machines_file.close()
        return known

    def machine_is_known(self, mac):
        return mac in self.known_machines

    def scan_all_machines(self):
        process_output = subprocess.check_output(["arp-scan","--interface=" + self.interface, "--localnet"])
        arr = process_output.strip().split('\n')
        arr = arr[2:len(arr) - 3]

        all_machines = []
        for line in arr: #ip\tmac address\tname
            all_machines.append(self.machine_array_to_hash(line.split('\t')))
        return all_machines

    def machine_array_to_hash(self, array):
        return dict(zip(['ip', 'mac', 'name'], array))