class Doggo:
  # constructor - magic method
  def __init__(self):
    print("a new doggo appeared!")
    self.legs = 4
    self.sound = "bark"

  # regular method
  def make_sound(self):
    print(self.sound)

  # method modifying underlying value
  def grow_leg(self):
    self.legs += 1

  # reports back the state of the class
  def is_regular_dog(self):
    return self.legs == 4

rex = Doggo()
print(rex.make_sound())

jake = Doggo()
print(jake.is_regular_dog())
jake.grow_leg()
print(jake.is_regular_dog())


#what does it print?
print("Rex:", rex.legs)
print("Jake:", jake.legs)
