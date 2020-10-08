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
  def test_onAlert_outsideHuman2_sendsMessage(self, send_message_mock):
    alert = Alert("outside", "human", 2)
    self.emailer.on_alert(alert)
    send_message_mock.assert_called_once_with(
      "quentin@example.com",
      "Alert",
      "What: human; Where: ouside; Level: 2"
    )
    #test for call content

  @patch.object(Emailer, "_send_message")
  def test_onAlert_outsideHuman1_sendsMessage(self, send_message_mock):
    alert = Alert("outside", "human", 1)
    self.emailer.on_alert(alert)
    send_message_mock.assert_not_called()

    



if __name__ == "__main__":
  unittest.main()