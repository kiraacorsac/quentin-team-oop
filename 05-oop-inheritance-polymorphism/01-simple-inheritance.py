class Animal:
  def walk(self):
    print("Animal is walking")

class Doggo(Animal):
  def bark(self):
    print("Dog is barking")
  


regular_animal = Animal()
regular_animal.walk()
# regular_animal.bark()

rex = Doggo()
rex.walk()
rex.bark()

print(regular_animal, type(regular_animal))
print(rex, type(rex))

print("Instances:")
print(isinstance(rex, Animal), isinstance(regular_animal, Animal))
print(isinstance(rex, Doggo), isinstance(regular_animal, Doggo))


print()
print("Types:")
print(type(rex) == Animal, type(regular_animal) == Animal)
print(type(rex) == Doggo, type(regular_animal) == Doggo)