class Doggo:
  def __init__(self):
    self.legs = 4
    self.sound = "Bark"

jake = Doggo()
jake.legs = -1 # a bug!
print(jake.legs)

jake.sound = "meow"
print(jake.sound)