class Animal():
  def move(self):
    self.__turn_head()
    print("Animal is moving")

  def __turn_head(self):
    print("Head turned")

class Doggo(Animal):
  def bark(self):
    print("Bark!")

  def wag_tail(self):
    # not available, throws exception
    # self.__turn_head()
    self._Animal__turn_head()
    print("Wagging tail")

class Cat(Animal):
  def meow(self):
    print("Meow!")

class Human(Animal):
  # barn = []
  def __init__(self):
    self.barn = []

jake = Doggo()
jake.bark()
jake.move()
jake.wag_tail()

rex = Doggo()

whisky = Cat()
whisky.meow()
whisky.move()

genericAnimal = Animal()

quentin = Human()
quentin.barn.append(jake)
quentin.barn.append(whisky)
quentin.barn.append(genericAnimal)
quentin.barn.append(rex)

laco = Human()

print("----")
for animal in laco.barn:
  if isinstance(animal, Doggo) == True:
    animal.bark()
  else:
    print("not a dog, unable to bark")
print("----")


print(isinstance(jake, Doggo))
print(isinstance(jake, Animal))
print(isinstance(jake, Cat))
print(isinstance(genericAnimal, Doggo))
