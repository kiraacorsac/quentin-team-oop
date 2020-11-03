class MotionDetector:
  def __init__(self, where, security_system):
    self.where = where
    self.security_system = security_system


  def create_alert(self):
    self.security_system.create_alert(None, self.where, 1)