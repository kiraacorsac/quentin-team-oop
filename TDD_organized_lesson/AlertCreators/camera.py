class Camera:
  '''
  name: String
  security_system: SecuritySystem
    - securtiy system where the camera is registered 

  where: [String]
    - specifies where the camera could be pointnig
  
  night_mode: Bool
    - camera is able to create alerts during night but not during the day

  is_connected(): Bool
    - retrurns true if security_system is not none

  detect_movement(): void
    - if it does and conditions favorable, call create_alert(), specifing where

  create_alert(): void
    - pass alert to security system


  (recording)
  '''
  def __init__(self, name, where):
    self.name = name
    self.where = where
    self.security_system = None

  

  def is_connected(self):
    if self.security_system is not None:
      return True
    else:
      return False
    
    