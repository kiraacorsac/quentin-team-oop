import unittest
from unittest.mock import patch 
from TDD_organized_lesson.AlertHandlers.doggo import Doggo
from TDD_organized_lesson.security_system import SecuritySystem

class SecuritySystemTest(unittest.TestCase):
  def test_registerHandler_doggo_isInHandlers(self):
    security =  SecuritySystem()
    doggo = Doggo("Jake")

    security.registerHandler(doggo)

    self.assertIn(doggo, security.handlers)
  
  def test_registerHandler_integer_raisesTypeError(self):
    security =  SecuritySystem()

    with self.assertRaises(TypeError):
      security.registerHandler(5)



  @patch.object(Doggo, "handle_alert")
  def test_alertCreated_doggoRegistred_doggoHandleAlert(self, handle_alert_mock):
    security =  SecuritySystem()
    doggo = Doggo("Jake")
    security.registerHandler(doggo)

    security.createAlert("outside", "human", 3)

    handle_alert_mock.assert_called_once()
    

  
