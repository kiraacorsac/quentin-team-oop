from TDD_Organized.AlertHandlers.alert_handler import AlertHandler

class SecuritySystem:
  def __init__(self):
    self.alert_handlers = []
    self.alert_creators = []

  def register_handler(self, alert_handler):
    if not isinstance(alert_handler, AlertHandler):
      raise TypeError("alert_handler needs to inherit from AlertHandler abstract class")
    self.alert_handlers.append(alert_handler)

  def raiseAlert(self, alert):
    for handler in self.alert_handlers:
      handler.handle_alert(alert)

  def install(self, alert_creator):
    self.alert_creators.append(alert_creator)
    alert_creator.install(self)