import os
import unittest
from network_alert import Persistance

FILE = os.path.expanduser("~/test_data")

test_data = [
    {'mac': 't1', 'ip': 'i1', 'name': 'n1'},
    {'mac': 't2', 'ip': 'i2', 'name': 'n2'},
    {'mac': 't3', 'ip': 'i3', 'name': 'n3'},
]


class TestPersistance(unittest.TestCase):

    def setUp(self):
        self.persistance = Persistance(FILE)

    def tearDown(self):
        if os.path.exists(FILE):
            os.remove(FILE)

    def test_save(self):
        device_data = {'mac': 'mac', 'ip': 'ip', 'name': 'name'}
        self.persistance.save(device_data)
        assert device_data in self.persistance.all()

    def test_all(self):
        for t in test_data:
            self.persistance.save(t)

        for t in test_data:
            assert t in self.persistance.all()

    def test_all_macs(self):
        for t in test_data:
            self.persistance.save(t)

        for t in [m['mac'] for m in test_data]:
            assert t in self.persistance.all_macs()

    def test_clear(self):
        for t in test_data:
            self.persistance.save(t)

        self.persistance.clear()
        assert len(self.persistance.all()) == 0
