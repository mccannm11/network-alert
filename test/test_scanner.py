import os
import unittest
from network_alert import Scanner
from .static import raw_arp_scan_output, parsed_arp_scan_output

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
        if not 'TRAVIS' in os.environ:
            self.assertNotEqual(self.scanner.run_subprocess(), None)

    def test_parse_devices(self):
        self.assertEqual(
            self.scanner.parse_devices(raw_arp_scan_output),
            parsed_arp_scan_output
        )

    def test_scan(self):
        if not 'TRAVIS' in os.environ:
            self.scanner.scan()
            self.assertNotEqual(self.scanner.devices, None)
