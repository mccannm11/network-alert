from network_alert import Client, Scanner, Mailer, Persistance
from mock import Mock, call
import unittest

class TestClient(unittest.TestCase):
	def setUp(self):
		# mocks
		self.mailer = Mailer('server', 'recipients', 'sender')
		self.scanner = Scanner('wlan0')
		self.persistance = Persistance('test_file')

		self.scanner.scan = Mock(return_value=self.scanner)
		self.scanner.devices = [{'mac': 'mac', 'ip': 123, 'name': 'name'}]
		self.persistance.save = Mock(return_value=None)
		self.persistance.all = Mock(return_value=['123','234'])

		self.client = Client(self.scanner, self.mailer, self.persistance)

	def test_unknown(self):
		expected = [d for d in self.client.all() if d['mac'] not in self.client.known()]
		assert self.client.unknown() ==  expected

	def test_known(self):
		assert self.client.known() == self.persistance.all()

	def test_all(self):
		assert self.client.all() == self.scanner.devices

	def test_learn(self):
		self.client.learn()
		expected = [call(self.scanner.devices[0]['mac'])]
		assert self.client.persistance.save.call_args_list == expected

	def test_alert(self):
		self.client.learn = Mock(return_value=None)
		self.mailer.send_warning_message = Mock(return_value=True)

		self.client.alert()

		self.client.mailer.send_warning_message.assert_called_once()
		self.client.learn.assert_called_once()

