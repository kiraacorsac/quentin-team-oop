import unittest
from doggo import Doggo

class DoggoTest(unittest.TestCase):
  def test_doggoName_nameSet_returnsName(self):
    doggo = Doggo("Jake")
    self.assertEqual(doggo.name, "Jake")

  def test_doggoName_complexNameSet_returnsName(self):
    doggo = Doggo("Mr. Puppet")
    self.assertEqual(doggo.name, "Mr. Puppet")

  def test_doggoName_nameSetEmptyString_raisesError(self):
    with self.assertRaises(ValueError):
      doggo = Doggo("")

  def test_doggoName_nameSetNotAlphabetic_raisesError(self):
    with self.assertRaises(ValueError):
      doggo = Doggo("!!!")

  def test_doggoName_nameChanged_raisesError(self):
    doggo = Doggo("Something in line")
    with self.assertRaises(Exception):
      doggo.name = "Something new"

  def test_sound_soundSet_returnSound(self):
    doggo = Doggo("Jake")
    doggo.sound = "bark"
    self.assertEqual(doggo.sound, "bark")

  def test_sound_default_exist(self):
    doggo = Doggo("Jake")
    self.assertEqual(doggo.sound, "Bark!")

  def test_sound_empty_raisesError(self):
    doggo = Doggo("Jake")
    with self.assertRaises(ValueError):
      doggo.sound = ""

  def test_doggoNumLegs_default_greaterThanOrEqual0(self):
    doggo = Doggo("Jake")
    self.assertGreaterEqual(doggo.num_legs, 0)


if __name__ == "__main__":
  unittest.main()