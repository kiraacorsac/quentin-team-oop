class Doggo:
  def __init__(self):
    self.legs = 5
    self.has_tail = True


  def make_sound(self):
    print("bark")

  def run(self):
    print("running...")


dunco = Doggo()
print(dunco.legs)

rex = Doggo()
rex.legs = 4
print(rex.legs)
print(dunco.legs)
