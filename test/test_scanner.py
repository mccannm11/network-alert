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

if __name__ == '__main__':
    unittest.main()