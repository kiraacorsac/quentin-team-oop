
# class describes how objects of that class will look
class Doggo:
  def __init__(self):
    # attributes
    self.legs = 4
    self.sound = "bark"

# object will have all the attributes of the class
rex = Doggo()
print(rex.sound)

# notexistent attribute
print(rex.collar)