class LoudCreature:
  def __init__(self):
    print("LoudCreature init")

  def make_sound(self):
    print("Creature making a sound")

class MovingCreature:
  def __init__(self):
    print("MovingCreature init")
    self.leg_number = 4

  def move(self):
    print("Creature moving around")


class Animal(MovingCreature, LoudCreature):
  def __init__(self):
    super().__init__()
    # DONT USE THIS PLEASE!
    LoudCreature.__init__(self)
    print("Animal init")

  def wag_tail(self):
    print("Animal wagging tail")


animal = Animal()
animal.make_sound()
animal.move()
animal.wag_tail()
print(animal.leg_number)