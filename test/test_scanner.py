import unittest
from network_alert import Scanner

INTERFACE = 'wlan0'

class TestScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = Scanner(INTERFACE)

    def test_device_array_to_hash(self):
        array = ['0.0.0.0', 'sd:34:df:45:df', 'Computer']
        hash = self.scanner.device_array_to_hash(array)
        self.assertEqual(hash['ip'], '0.0.0.0')
        self.assertEqual(hash['mac'], 'sd:34:df:45:df')
        self.assertEqual(hash['name'], 'Computer')

    def test_run_subprocess(self):
        self.assertNotEqual(self.scanner.run_subprocess(), None)

    def test_parse_devices(self):
        self.assertEqual(self.scanner.parse_devices(raw_output), parsed_output)

    def test_scan(self):
        self.scanner.scan()
        self.assertNotEqual(self.scanner.devices, None)


raw_output = """Interface: wlan0, datalink type: EN10MB (Ethernet)
Starting arp-scan 1.8.1 with 256 hosts (http://www.nta-monitor.com/tools/arp-scan/)
192.168.1.1\t20:aa:4b:dc:85:04\t(Unknown)
192.168.1.118\te4:ce:8f:12:13:48\tApple Inc
192.168.1.120\t90:18:7c:10:e7:c4\t(Unknown)
192.168.1.148\t00:26:bb:1b:17:f5\tApple, Inc
192.168.1.103\ta8:fa:d8:f1:dc:a3\t(Unknown) (DUP: 1)

5 packets received by filter, 0 packets dropped by kernel
Ending arp-scan 1.8.1: 256 hosts scanned in 1.391 seconds (184.04 hosts/sec). 5 responded
"""

parsed_output = [
    {'ip': '192.168.1.1', 'mac': '20:aa:4b:dc:85:04', 'name': '(Unknown)' },
    {'ip': '192.168.1.118', 'mac': 'e4:ce:8f:12:13:48', 'name': 'Apple Inc' },
    {'ip': '192.168.1.120', 'mac': '90:18:7c:10:e7:c4', 'name': '(Unknown)' },
    {'ip': '192.168.1.148', 'mac': '00:26:bb:1b:17:f5', 'name': 'Apple, Inc' },
    {'ip': '192.168.1.103', 'mac': 'a8:fa:d8:f1:dc:a3', 'name': '(Unknown) (DUP: 1)'}
]
