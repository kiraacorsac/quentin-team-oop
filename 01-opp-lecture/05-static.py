class Doggo:
  dog_count = 0
  __legs = 4

  def __init__(self, doggo_name):
    # attributes = state
    print('initing a new doggo')
    self.sound = "bark"
    self.name = doggo_name
    Doggo.dog_count += 1


print(Doggo.dog_count)
jake = Doggo("Jake")

print(Doggo.dog_count)
rex = Doggo("Rex")
print(Doggo.dog_count)

print(jake.dog_count)
print(rex.dog_count)

dunco = Doggo("Dunco")
print(dunco.dog_count)


Doggo.__legs = 5

print(rex.legs)


