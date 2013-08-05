import unittest
import os
import sys

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.abspath(file_path))

from scanner import Scanner

# In place of config files
#TODO: create a test environment once ive got htis working
FILE = '../known_machines'
INTERFACE = "wlan0"
PATH = "./"

class TestScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = Scanner(FILE, INTERFACE, PATH)

    def tearDown(self):
        try:
            os.remove(FILE)
        except OSError, e:
            pass

    def test_add_to_known_machines(self):
        mac = '00:1e:8c:4f:10:43'
        file = open(FILE, 'a+')
        self.scanner.add_to_known_machines(mac)
        self.assertEqual(len(file.read().split('\n')), 2)

    # Some quick and dirty test data
    def test_filter_unknown_machines(self):
        self.scanner.all_machines = [
            {'mac':'00:1e:8c:4f:10:43'},
            {'mac': '00:1e:8c:4f:10:44'},
            {'mac': '00:1e:8c:4f:10:45'},
            {'mac': '00:1e:8c:4f:10:46'},
        ]
        self.scanner.known_machines = ['00:1e:8c:4f:10:43','00:1e:8c:4f:10:44', '00:1e:8c:4f:10:45']
        unknown = self.scanner.filter_unknown_machines()
        self.assertEqual(len(unknown), 1)
        self.assertEqual(unknown[0]['mac'], '00:1e:8c:4f:10:46')

    def test_read_known_machines(self):
        open(FILE, 'a+').write('00:1e:8c:4f:10:41\n00:1e:8c:4f:10:42\n00:1e:8c:4f:10:43')
        self.assertEqual(len(self.scanner.read_known_machines()), 3)
        self.assertEqual(self.scanner.read_known_machines()[0], '00:1e:8c:4f:10:41')

    def machine_is_known(self):
        self.scanner.known_machines = ['hello', 'salut', 'buenos dias']
        self.assertTrue(self.scanner.machine_is_known('hello'))
        self.assertTrue(self.scanner.machine_is_known('salut'))
        self.assertTrue(self.scanner.machine_is_known('buenos dias'))
        self.assertFalse(self.scanner.machine_is_known('not in list'))

    def scan_all_machines(self):
        # errr, im gonna have to pass on this one
        pass

    def test_machine_array_to_hash(self):
        array = ['0.0.0.0', 'sd:34:df:45:df', 'Computer']
        hash = self.scanner.machine_array_to_hash(array)
        self.assertEqual(hash['ip'], '0.0.0.0')
        self.assertEqual(hash['mac'], 'sd:34:df:45:df')
        self.assertEqual(hash['name'], 'Computer')

if __name__ == '__main__':
    unittest.main()