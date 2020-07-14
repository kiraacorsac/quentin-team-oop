class Animal:
  def __init__(self, name):
    self.name = name

  def walk(self):
    print(self.name, "is walking")

class Doggo(Animal):
  def __init__(self, name):
    Animal.__init__(self, name)

  def bark(self):
    print(self.name, "barks!")

# -______________________________


# class Animal:
#   def walk():
#     print("Animal is walking")

# class Doggo:
#   def walk():
#     print("Animal is walking")

#   def bark():
#     print("bark!")

jake = Doggo("Jake")
jake.bark()
jake.walk()
print("Doggo's name:", jake.name)

regular_animal = Animal("Alice")
regular_animal.walk()

print(type(jake))
print(type(regular_animal))
print(isinstance(regular_animal, Doggo))


jake.walk()