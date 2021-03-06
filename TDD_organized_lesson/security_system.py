from TDD_organized_lesson.alert import Alert
from TDD_organized_lesson.AlertHandlers.alert_handler import AlertHandler
from TDD_organized_lesson.AlertCreators.alert_creator import AlertCreator

class SecuritySystem:
  def __init__(self):
    self.handlers = []
    self.creators = []

  def registerHandler(self, handler):
    if not isinstance(handler, AlertHandler):
      raise TypeError("Alert handler needs to derive from 'AlertHandler' class")

    self.handlers.append(handler)

  def createAlert(self, where, what, level):
    alert = Alert(where, what, level)

    for handler in self.handlers:
      handler.handle_alert(alert)

  def registerCreator(self, creator):
    if not isinstance(creator, AlertCreator):
      raise TypeError("Alert creator needs to derive from 'AlertCreator' class")
    self.creators.append(creator)
    creator.security_system = self