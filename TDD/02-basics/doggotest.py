import unittest
from doggo import Doggo

class Doggo(unittest.TestCase):
  def test_doggo_hasName_returnsName(self):
    jake = Doggo("Jake")
    self.assertEqual(jake.name, "Jake")

  def test_doggo_defaultBark_returnsBark(self):
    jake = Doggo("Jake")
    self.assertEqual(jake.bark(), "Bark!")

  def test_doggo_changedBark_returnsBark(self):
    jake = Doggo("Jake")
    jake.sound = "Woof!"
    self.assertEqual(jake.bark(), "Woof!")

  def test_doggo_emptyBarkSound_throwsCannotBeEmpty(self):
    jake = Doggo("Jake")
    try:
      jake.sound = ""
    except Exception as e:
      return
    self.fail("Did not throw exception")

    # with self.assertRaises

  def test_doggo_emptyBarkSound_throwsCannotBeEmpty2(self):
    jake = Doggo("Jake")
    with self.assertRaises(Exception):
      jake.sound = ""
    

  @unittest.expectedFailure
  def test_doggo_emptyBarkSound_throwsCannotBeEmpty3(self):
    jake = Doggo("Jake")
    jake.sound = ""
    self.assertEqual(jake.bark(), "")

  


if __name__ == "__main__":
  unittest.main()