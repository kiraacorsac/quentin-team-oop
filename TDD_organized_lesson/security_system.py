from TDD_organized_lesson.alert import Alert

class SecuritySystem:
  def __init__(self):
    self.handlers = []

  def registerHandler(self, handler):
    self.handlers.append(handler)

  def createAlert(self, where, what, level):
    alert = Alert(where, what, level)

    for handler in self.handlers:
      handler.handle_alert(alert)