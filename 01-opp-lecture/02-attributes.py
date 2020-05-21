class Collar:
  def __init__(self):
    self.length = 40
    self.diameter = 4


# blueprint for object
class Doggo:
  def __init__(self):
    self.legs = 4
    self.sound = "bark"
    self.collar = Collar()


jake = Doggo()
rex = Doggo()

jake2 = jake

jake.legs = 5

print(rex.legs)
print(jake.legs)
print(jake2.legs)

print(jake.collar.diameter)