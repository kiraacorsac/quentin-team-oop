class LoudCreature:
  def __init__(self, sound, **kwargs):
    print("LoudCreature start")
    super(LoudCreature, self).__init__(**kwargs)
    self.sound = sound
    print("LoudCreature end")

  def make_sound(self):
    print(self.sound)

class MovingCreature:
  def __init__(self, speed, leg_number, **kwargs):
    print("MovingCreature start")
    super(MovingCreature, self).__init__(**kwargs)
    print(speed)
    print("MovingCreature end")

  def move(self):
    print("Creature moving around")

class FlyingCreature:
  def __init__(self, feathered, **kwargs):
    print("FlyingCreature start")
    super(FlyingCreature, self).__init__(**kwargs)

    self.feathered = feathered
    print(self.feathered)
    print("FlyingCreature end")

  def lose_feather(self):
    pass

class Animal(FlyingCreature, MovingCreature, LoudCreature):
  def __init__(self, name, anim_feathered, anim_sound, anim_speed, anim_leg_number):
    print("Animal start")
    # super(Animal, self).__init__(feathered=feathered, leg_number=leg_number, 
    #                             sound=sound, speed=speed)
    super(Animal, self).__init__(
      feathered= anim_feathered,
      leg_number = anim_leg_number,
      speed = anim_speed,
      sound = anim_sound
    )
    # # DONT USE THIS PLEASE!
    # LoudCreature.__init__(self)
    self.name = name
    print("Animal end")
  
  def wag_tail(self):
    print("Animal wagging tail")


animal = Animal("Jake", False, "barks", 10, 4)
animal.make_sound()
animal.move()
animal.wag_tail()
# # print(animal.leg_number)




# def divide_nums(numerator, denominator):
#   return numerator/denominator


# print(divide_nums(denominator=10, numerator=5))