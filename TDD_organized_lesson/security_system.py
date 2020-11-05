from TDD_organized_lesson.alert import Alert
from TDD_organized_lesson.AlertHandlers.alert_handler import AlertHandler

class SecuritySystem:
  def __init__(self):
    self.handlers = []

  def registerHandler(self, handler):
    if not isinstance(handler, AlertHandler):
      raise TypeError("Alert handler needs to derive from 'AlertHandler' class")

    self.handlers.append(handler)

  def createAlert(self, where, what, level):
    alert = Alert(where, what, level)

    for handler in self.handlers:
      handler.handle_alert(alert)