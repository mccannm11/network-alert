from network_alert import Mailer

import unittest
import network_alert

SERVER = 'localhost'
RECIPIENTS = 'test@test.com'
SENDER = 'sender@sender.com'

class TestMailer(unittest.TestCase):
	def setUp(self):
		self.mailer = Mailer(SERVER, RECIPIENTS, SENDER)

	def test_send_warning_message(self):
		## if no macs sent, it should return
		assert self.mailer.send_warning_message([]) == False

	def test_build_message(self):
		message = self.mailer.build_message([{
				'mac':'mac',
				'ip': '123',
				'name': 'name',
			}])

		assert message == "\n MAC: mac Name: name IP: 123"