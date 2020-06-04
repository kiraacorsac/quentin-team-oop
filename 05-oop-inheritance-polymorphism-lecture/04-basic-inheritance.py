
class Animal:
  def __init__(self, name):
    print('initing a new animal')
    self.head_count = 0
    self.name = name
  
  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, new_name):
    if(len(new_name) < 4):
      raise Exception("Animal's name has to be at least 4 characters")
    
    self.__name = new_name



  def walk(self):
    print(self.name, "is walking")

  def head_turn(self):
    if(self.is_zombie()):
      print(self.name, "turning head")
    else:
      print(self.name, "has no heads to turn")

  def is_zombie(self):
    return self.head_count >= 1


class Doggo(Animal):
  def __init__(self, name, legs):
    super().__init__(name)
    print('initing a Doggo')
    self.legs = legs
    


# animal = Animal("robbo")
# animal.walk()
# animal.head_turn()

jake = Doggo("Jake", 4)
jake.name = "Rex"

print(jake.name)

# rex.walk()
# rex.head_turn()