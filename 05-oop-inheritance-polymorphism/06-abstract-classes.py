# animal without any specie cannot exist!
# every animal makes sound and moves, but we don't know how without a spiece

from abc import ABC, abstractmethod

class Mammal(ABC):
  def breath(self):
    print("Breathing using lungs")

  @abstractmethod
  def make_sound(self):
    pass
  
  @abstractmethod
  def move(self):
    pass


class Doggo(Mammal):
  def make_sound(self):
    print("Bark")

  def move(self):
    print("Running")


class Bat(Mammal):
  def make_sound(self):
    print("*ultrasound noises*")

  def move(self):
    print("Flying")


# raises
# mammal = Mammal()
 
dog = Doggo()
dog.breath()
dog.make_sound()
dog.move()

bat = Bat()
bat.breath()
bat.make_sound()
bat.move()


