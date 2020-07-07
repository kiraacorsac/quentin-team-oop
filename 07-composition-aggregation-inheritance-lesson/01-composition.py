class Doggo:
  def __init__(self, name, collar, legs=4):
    self.name = name
    self.collar = collar
    self.legs = legs

  
class Collar:
  def __init__(self, length, material):
    self.length = length
    self.material = material
    self.opened = False

  def open(self):
    self.opened = True
    print("Undone the collar")



jake = Doggo("Jake", Collar(10, "leather"))

rexes_collar = Collar(15, "cloth")
rex = Doggo("Rex", rexes_collar)
dunco = Doggo("Dunco", rexes_collar)


print(dunco.collar.opened)
print(rex.collar.opened)
print(jake.collar.opened)
# rex.collar.open()
dunco.collar.open()
print(dunco.collar.opened)
print(rex.collar.opened)
print(jake.collar.opened)