class Doggo:
  # method = action
  def __init__(self, age, doggo_name):
    # attributes = state
    print('initing a new doggo')
    self.legs = 4
    self.sound = "bark"
    self.age = age
    self.name = doggo_name

  def get_doggo_attributes(self):
    return self.legs, self.sound, self.age, self.name

  def set_number_of_legs(self, new_leg_number = 4):
    self.legs = new_leg_number

  
rex = Doggo(10, "Rex")
jake = Doggo(doggo_name="Jake", age=10)

print(jake.get_doggo_attributes())

jake.set_number_of_legs(5)
print(jake.legs)

jake.set_number_of_legs()
print(jake.legs)

print(jake.name)