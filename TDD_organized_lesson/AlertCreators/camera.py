class Camera:
  '''
  name: String
  security_system: SecuritySystem
    - securtiy sytem where the camera is registered 

  where: [String]
    - specifies where the camera could be pointnig
  
  night_mode: Bool
    - camera is able to create alerts during night but not during the day

  is_connected(): Bool
    - retrurns true if security_system is not none

  detect_movement():
    - if it does and conditions favorable, call create_alert() on security_system


  (recording)
  '''