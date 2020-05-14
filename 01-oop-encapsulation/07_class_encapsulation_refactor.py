class Doggo:
  def __init__(self):
    self.legs = 4


class DoggoFix:
  def __init__(self):
      self.legs = 4

  @property
  def legs(self):
    return self.__legs
  
  @legs.setter
  def legs(self, new_leg_count):
    if(new_leg_count < 0):
      raise Exception("Leg count cannot be negative")
    self.__legs = new_leg_count



#code already in use - how to avoid touching it ?
jake = DoggoFix()
jake.legs = -1 # a bug!
print(jake.legs)

