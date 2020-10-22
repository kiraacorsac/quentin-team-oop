from TDD_Organized.security_system import SecuritySystem
import unittest
from TDD_Organized.AlertHandlers.doggo import Doggo
from TDD_Organized.alert import Alert
from unittest.mock import patch
from TDD_Organized.AlertHandlers.emailer import Emailer
from TDD_Organized.AlertHandlers.alert_handler import AlertHandler


class SecuritySystemTest(unittest.TestCase):
  def setUp(self):
    self.simple_system = SecuritySystem()

  def test_registerHandler_addDoggo_registred(self):
    doggo = Doggo("Jake")
    self.simple_system.register_handler(doggo)
    self.assertIn(doggo, self.simple_system.alert_handlers)

  def test_registerHandler_addString_throws(self):
    string = "This is not an alert handler." 
    with self.assertRaises(TypeError):
      self.simple_system.register_handler(string)
    
  @patch.object(Doggo, "handle_alert")
  def test_raiseAlert_oneHanlder_handlerCalled(self, handle_alert_mock):
    doggo_mock = Doggo("Jake")
    alert = Alert("where", "what", 0)
    self.simple_system.register_handler(doggo_mock)
    self.simple_system.raiseAlert(alert)
    handle_alert_mock.assert_called_once()
    
  @patch.object(Doggo, "handle_alert")
  @patch.object(Emailer, "handle_alert")
  def test_raiseAlert_twoHanlders_handlersCalled(self, doggo_handle_alert_mock, emailer_handle_alert_mock):
    doggo = Doggo("Jake")
    emailer = Emailer("Rex")
    alert = Alert("where", "what", 0)
    self.simple_system.register_handler(doggo)
    self.simple_system.register_handler(emailer)
    self.simple_system.raiseAlert(alert)
    doggo_handle_alert_mock.assert_called_once()
    emailer_handle_alert_mock.assert_called_once()