class MotionDetector:
  def __init__(self, where):
    self.where = where
    self.security_system = None


  def create_alert(self):
    if self.is_installed:
      self.security_system.create_alert(None, self.where, 1)
    else:
      raise Exception("Can not create alert, this motion detector is not installed.")

  def is_installed(self):
    return self.security_system

  def install(self, security_system):
    self.security_system = security_system