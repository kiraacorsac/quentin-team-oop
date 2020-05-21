class Doggo:
  # method = action
  def __init__(self):
    # attributes = state
    print('initing a new doggo')
    self.legs = 4
    self.sound = "bark"
    

  # method that does not change the object nor returns value
  def make_sound(self):
    print(self.sound)

  # modifying state
  def grow_leg(self):
    self.legs += 1

  def is_regular_dog(self):
    if(self.legs == 4):
      return True
    else:
      return False

jake = Doggo()
rex = Doggo()
jake.make_sound()

def make_sound(doggo):
  print(doggo.sound)


make_sound(jake)

print(jake.legs)
jake.grow_leg()
print(jake.legs)


print(jake.is_regular_dog())
print(rex.is_regular_dog())