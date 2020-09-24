import unittest
from unittest.mock import patch, call, mock_open

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

  
  def test_doggoNumLegs_setLessThan0_raisesError(self):
    doggo = Doggo("Jake")
    with self.assertRaises(ValueError):
      doggo.num_legs = -1

  @patch('builtins.print')
  def test_bark_default_prints(self, print_mock):
    doggo = Doggo("Jake")
    doggo.bark()

    self.assertListEqual(print_mock.mock_calls, [call("Jake barks: Bark!")])


  @patch('builtins.open', new_callable=mock_open())
  def test_makeNote_default_writes(self, file_mock):
    doggo = Doggo("Jake")
    doggo.make_note()

    file_mock.assert_called_once_with("note.txt", 'w')
    file_mock("note.txt", 'w').write.assert_called_once_with("Something suspicious!")

if __name__ == "__main__":
  unittest.main()