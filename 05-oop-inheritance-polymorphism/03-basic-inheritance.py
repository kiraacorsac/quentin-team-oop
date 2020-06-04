#show how not calling constructor works first,


class Animal:
  def __init__(self, name):
    print('initing a new animal')
    if(len(name) < 4):
      raise Exception("Animal's name has to be at least 4 characters")
    self.name = name
  
  def walk(self):
    print(self.name, "is walking")

class Doggo(Animal):
  def __init__(self, age, doggo_name):
    super().__init__(doggo_name)
    print('initing a new doggo')
    self.legs = 4
    self.sound = "bark"
    self.age = age
    # self.name = doggo_name

  def get_doggo_attributes(self):
    return self.legs, self.sound, self.age, self.name

  def set_number_of_legs(self, new_leg_number = 4):
    self.legs = new_leg_number


jake = Doggo(7, "Jak")
jake.walk()

