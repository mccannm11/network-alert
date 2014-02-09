import os
import unittest
from network_alert import Persistance

FILE = "test_data"
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
        self.persistance.save({'mac': 'mac', 'ip': 'ip', 'name': 'name'})
        assert 'mac' in self.persistance.all()

    def test_all(self):
        [self.persistance.save(d) for d in test_data]
        assert 't1' in self.persistance.all()

    def test_clear(self):
        [self.persistance.save(d) for d in test_data]
        self.persistance.clear()
        assert len(self.persistance.all()) == 0
