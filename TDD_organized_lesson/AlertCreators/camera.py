class Camera:
  def __init__(self, where, security_system):
    self.where = where
    self.security_system = security_system


  def create_alert(self, what):
    self.security_system.create_alert(what, self.where, 2)