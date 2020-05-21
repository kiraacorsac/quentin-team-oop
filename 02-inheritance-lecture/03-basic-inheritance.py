

class Animal:
  def __init__(self, name, age, legs, sound):
    print('initing a new animal')
    if(len(name) < 4):
      raise Exception("Animal's name has to be at least 4 characters")
    self.name = name


    self.age = age
    self.legs = legs
    self.sound = sound
  
  def walk(self):
    print(self.name, "is walking")

class Doggo(Animal):
  def __init__(self, age, doggo_name):
    Animal.__init__(self, doggo_name, age, 4, "bark")
    print('initing a new doggo')

    self.tail_wag_speed = 10
    # self.name = doggo_name

  def get_doggo_attributes(self):
    return self.legs, self.sound, self.age, self.name

  def set_number_of_legs(self, new_leg_number = 4):
    self.legs = new_leg_number


jake = Doggo(7, "Jake")
jake.walk()
jake.
print(jake.__dict__)
