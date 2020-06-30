class HelloThere:
  pass

class HelloThereProvider:
  def __new__(cls):
    print("Creating new hello there")
    return HelloThere()

  def test(self):
    print("Testing...")


new_hello = HelloThereProvider()
# new_hello.test()
print(new_hello)