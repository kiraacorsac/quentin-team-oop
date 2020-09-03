from greeter import Greeter
import unittest


class GreeterTests(unittest.TestCase):

  def test_greeterTest(self):
    greeter = Greeter()
    greeting = greeter.greet("Juraj")
    self.assertEqual(greeting, "Hello, Juraj")
  

  def test_greet_notString_raises(self):
    greeter = Greeter()

    try:
      greeting = greeter.greet(10)
    except TypeError as e:
      return
    
    self.fail("No exception thrown")


if __name__ == "__main__":
  unittest.main()