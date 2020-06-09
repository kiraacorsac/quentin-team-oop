class LoudCreature:
  def __init__(self):
    print("LoudCreature start")
    super(LoudCreature, self).__init__()
    print("LoudCreature end")

  def make_sound(self):
    print("Creature making a sound")

class MovingCreature:
  def __init__(self):
    print("MovingCreature start")
    super(MovingCreature, self).__init__()
    self.leg_number = 4
    print("MovingCreature end")

  def move(self):
    print("Creature moving around")

class FlyingCreature(MovingCreature):
  def __init__(self):
    print("FlyingCreature start")
    super(FlyingCreature, self).__init__()
    print("FlyingCreature end")


class Animal(FlyingCreature, LoudCreature):
  def __init__(self):
    print("Animal start")
    super(Animal, self).__init__()
    # # DONT USE THIS PLEASE!
    # LoudCreature.__init__(self)
    print("Animal end")

  def wag_tail(self):
    print("Animal wagging tail")


animal = Animal()
animal.make_sound()
animal.move()
animal.wag_tail()
# print(animal.leg_number)