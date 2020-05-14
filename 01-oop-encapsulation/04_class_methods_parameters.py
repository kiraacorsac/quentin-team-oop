class Doggo:
  
  def __init__(self, name):
    self.legs = 4
    self.sound = "bark"
    self.name = name

  def make_sound(self):
    print(self.sound)

  def grow_legs(self, new_legs):
    self.legs += new_legs

  # not valid, missing self
  # def grow_legs(new_legs):
  #   self.legs += new_legs


jake = Doggo()
jake.grow_legs(5)
print(jake.legs)

 # self - refences the object that we are calling the method on

def grow_legs(dog, new_legs):
  dog.legs += 1

grow_legs(jake)

# we can tie methods such as these to the class, that's what it's for!