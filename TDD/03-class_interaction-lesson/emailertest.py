import unittest
import smtplib
from emailer import Emailer
from alert import Alert
from unittest.mock import patch

class EmailerTest(unittest.TestCase):
  def setUp(self):
    self.emailer = Emailer("filip@example.com")
    self.emailer.alert_recipient = "quentin@example.com"


  @patch.object(smtplib.SMTP, 'sendmail')
  @patch('smtplib.SMTP')
  def test_sendMessage_simple_sends(self, sendmail_mock, server_mock):
    self.emailer._send_message("quentin@mail.cz", "hello", "there")
    sendmail_mock.assert_called_once()

  @patch.object(Emailer, "_send_message")
  def test_handleAlert_level2_emailSent(self, sendMessage_mock):
    alert = Alert("outside", "human", 2)

    self.emailer.handle_alert(alert)

    sendMessage_mock.assert_called_once()

if __name__ == "__main__":
  unittest.main()