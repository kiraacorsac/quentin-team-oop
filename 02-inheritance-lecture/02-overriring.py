class Animal:
  def __init__(self, name):
    self.name = name

  def walk(self):
    print(self.name, "is walking")

  def make_sound(self):
    print(self.name, "is making a sound")

class Doggo(Animal):
  def __init__(self, name):
    Animal.__init__(self, name)

  def make_sound(self):
    print(self.name, "barks!")


regular_animal = Animal("Alice")
regular_animal.make_sound()


jake = Doggo("Jake")
jake.make_sound()

