class Animal:
  def __init__(self, name):
    
    self.name = name

  def walk(self):
    print(self.name, "is walking")

  def make_sound(self):
    print(self.name,"making it's sound")

class Doggo(Animal):
  def make_sound(self):
    print(self.name, "is barking")
  


regular_animal = Animal("Alice")
regular_animal.walk()
regular_animal.make_sound()

rex = Doggo("Rex")
regular_animal.make_sound()
rex.make_sound()

### force rex to behave like regular animal?
Animal.make_sound(rex)