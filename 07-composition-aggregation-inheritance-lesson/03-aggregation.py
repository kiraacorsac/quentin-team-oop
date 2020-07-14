class Doggo:
  def __init__(self):
    self.tail = Tail()

  def __del__(self):
    print("Doggo Deleted")


class Tail:
  def wag(self):
    print("Wagging tail")

  def __del__(self):
    print("Tail Deleted")

def doggo_test():
  jake = Doggo()
  jake.tail.wag()

doggo_test()

print("Ending script...")