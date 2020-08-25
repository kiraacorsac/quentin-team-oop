import unittest
from greeter import Greeter

class GreeterTest(unittest.TestCase):
  def test_greeter_returns_expected(self):
    greeter = Greeter()
    self.assertEqual(greeter.greet("Quentin"), "Hello, Quentin")


if __name__ == "__main__":
  unittest.main()