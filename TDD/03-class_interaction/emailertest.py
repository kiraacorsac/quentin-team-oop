import unittest
import smtplib
from emailer import Emailer
from alert import Alert
from unittest.mock import patch

class EmailerTest(unittest.TestCase):
  
  @patch.object(smtplib.SMTP, 'sendmail')
  @patch('smtplib.SMTP')
  def test_sendMessage_simple_sends(self, sendmail_mock, server_mock):
    emailer = Emailer("kiraa@mail.cz")
    emailer._send_message("quentin@mail.cz", "hello", "there")
    server_mock.assert_called_once()

if __name__ == "__main__":
  unittest.main()