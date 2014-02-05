import unittest
from network_alert import Persistance

import os

FILE = "test_data"
test_data = ['t1', 't2', 't3', 't4']

class TestPersistance(unittest.TestCase):
	def setUp(self):
		self.persistance = Persistance(FILE)

	def tearDown(self):
		if os.path.exists(FILE):
			os.remove(FILE)

	def test_save(self):
		self.persistance.save('testing_123')
		assert 'testing_123' in self.persistance.all()

	def test_all(self):
		[self.persistance.save(d) for d in test_data]
		for t in test_data:
			assert t in self.persistance.all()

	def test_clear(self):
		[self.persistance.save(d) for d in test_data]
		self.persistance.clear()
		assert len(self.persistance.all()) == 0

