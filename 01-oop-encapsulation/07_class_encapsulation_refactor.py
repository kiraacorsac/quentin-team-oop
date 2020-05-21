class Doggo:
  def __init__(self):
    self.legs = 4
    self.sound = "Bark"


class DoggoFix:
  allowed_sounds = ["woof", "bark", "ruff", "yipp"]
  def __init__(self):
      self.legs = 4
      self.sound = "Bark"

  @property
  def legs(self):
    return self.__legs

  # how many times will run?
  @legs.setter
  def legs(self, new_leg_count):
    if(new_leg_count < 0):
      raise Exception("Leg count cannot be negative")
    self.__legs = new_leg_count

  @property
  def sound(self):
    return self.__sound
  
  @sound.setter
  def legs(self, new_sound):
    if(new_sound not in allowed_sounds):
      raise Exception("Diallowed dog sound")
    self.__sound = new_sound



#code already in use - how to avoid touching it ?
jake = DoggoFix()
jake.legs = -1 # a bug!
print(jake.legs)

jake.sound = "meow"
print(jake.sound)
