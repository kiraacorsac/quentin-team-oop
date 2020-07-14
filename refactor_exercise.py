class Doggo:
  def __init__(self):
    self.legs = 4

from abc import ABC, abstractmethod

class Backyard:
  def __init__(self, size):
    self.animals = []
    self.size = size


  def add_animal(self, animal):
    if(isinstance(animal, Animal)):
      self.animals.append(animal)

  def make_lound(self):
    for animal in self.animals:
      animal.make_sound()


class Animal(ABC):
  def __init__(self, name, legs):
    self.name = name
    self.legs = legs

  @abstractmethod
  def make_sound(self):
    pass

  @property
  def legs(self):
    return self.__legs

  @legs.setter
  def legs(self, new_leg_amount):
    if(new_leg_amount < 0):
      raise Exception("Not enough legs")
    self.__legs = new_leg_amount

class DoggoFix(Animal):
  def __init__(self, name):
    super().__init__(name, 4)

  def make_sound(self):
    print("Bark!")

  def wag_tail(self):
    print("Tail wag!")


class Cat(Animal):
  def __init__(self, name):
    super().__init__(name, 4)

  def purr(self):
    print("Purring.")

  def make_sound(self):
    print("Meow!")


doggo = DoggoFix("Jake")
print(doggo.legs)
doggo.legs = 5
doggo.make_sound()
print(doggo.legs)

alice = Cat("Alice")
alice.legs = 5
alice.make_sound()
print(alice.legs)

# animal = Animal("John", 0)


yard = Backyard(20)
yard.add_animal(alice)
yard.add_animal(doggo)
yard.add_animal(2)

print(yard.animals)
yard.make_lound()