import unittest
from doggo import Doggo

class DoggoTest(unittest.TestCase):
  def test_doggoName_nameSet_returnsName(self):
    doggo = Doggo("Jake")
    self.assertEqual(doggo.name, "Jake")

  def test_doggoName_nameSetEmptyString_raisesError(self):
    with self.assertRaises(ValueError):
      doggo = Doggo("")



if __name__ == "__main__":
  unittest.main()