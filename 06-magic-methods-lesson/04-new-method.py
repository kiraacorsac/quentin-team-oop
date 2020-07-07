class HelloThere:
  pass

class HelloThereProvider:
  def __new__(cls):
    print("Creating new hello there")
    return 5404

  def test(self):
    print("Testing...")


new_hello = HelloThereProvider()
print(type(new_hello))
# new_hello.test()
print(new_hello)