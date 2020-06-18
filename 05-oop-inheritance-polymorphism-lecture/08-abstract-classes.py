from abc import abstractmethod, ABC


class Animal(ABC):
  @abstractmethod
  def make_sound(self):
    pass

  @abstractmethod
  def move(self):
    pass

  def sleep(self):
    print("Zzzzz...")


class Doggo(Animal):
  def make_sound(self):
    print("Bark")

  def move(self):
    print("running")

class Bat(Animal):
  def make_sound(self):
    print("*ultrasonic noises*")

  def move(self):
    print("flying")


jake = Doggo()
jake.make_sound()
jake.sleep()

tom = Bat()
tom.make_sound()
tom.sleep()

generic_animal = Animal()
# generic_animal.make_soPund()