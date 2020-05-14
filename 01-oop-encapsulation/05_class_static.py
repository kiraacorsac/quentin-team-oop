class Doggo:
  what_am_i = "grown up pupper"
  dog_counter = 0

  # constructor
  def __init__(self, name):
    self.legs = 4
    self.sound = "bark"
    self.name = name
    Doggo.dog_counter += 1

  def make_sound(self):
    print(self.sound)

  def grow_legs(self, new_legs):
    self.legs += new_legs



print(Doggo.what_am_i)
print(Doggo.dog_counter)

rex = Doggo("Rex")

print(Doggo.dog_counter)
print(rex.dog_counter)

jake = Doggo("Jake")

print(Doggo.dog_counter)
print(rex.dog_counter)
print(jake.dog_counter)

