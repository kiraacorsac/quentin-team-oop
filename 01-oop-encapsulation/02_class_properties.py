


# class describes how objects of that class will look
class Doggo:
  def __init__(self):
    # attributes
    self.legs = 4
    self.sound = "bark"
    self.collar = None

class Collar:
  def __init__(self):
    self.length = 60

# object will have all the attributes of the class
rex = Doggo()
print(rex.sound)

print(rex.collar)
rex.collar = Collar()
print(rex.collar)

# notexistent attribute
print(rex.muzzle)

jake = Doggo()
jake.collar = Collar()
print(jake.collar == rex.collar)