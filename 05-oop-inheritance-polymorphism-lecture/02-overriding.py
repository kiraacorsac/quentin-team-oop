class LivingCreature():
  def make_sound(self):
    print("emit waves")

class Animal():
  def move(self):
    print("Animal is moving")
  
  def make_sound(self):
    print("Animal is making sound")

class Doggo(Animal):
  def make_sound(self):
    print("Bark!")

class Cat(Animal):
  pass
  # def make_sound(self):
  #   print("Meow!")


rex = Doggo()
whisky = Cat()

rex.make_sound()
whisky.make_sound()