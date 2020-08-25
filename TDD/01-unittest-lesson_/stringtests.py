import unittest


class StringTest(unittest.TestCase):
  # test_what_when_expected
  def test_upper_simpleSentence_UPPER(self):
    sentence = "Hello world."
    self.assertEqual(sentence.upper(), "HELLO WORLD.")

  def test_isupper_uppercase_true(self):
    word = "WORLD"
    self.assertTrue(word.isupper())

  def test_isupper_lowercase_false(self):
    word = "world"
    self.assertFalse(word.isupper())

  def test_isupper_mixedcase_false(self):
    word = "WORLd"
    self.assertFalse(word.isupper())

  def test_split_simpleSentence_splits(self):
    sentence = "Hello world."
    self.assertEqual(sentence.split(" "), ['Hello', "world."])

  def test_split_simpleSentenceOnNumber_raises(self):
    sentence = "Hello world."
    try:
      sentence.split(2)
    except TypeError:
      return
    self.fail("Splitting on 2 should result in an exception")

  def test_split_simpleSentenceOnNumber_raises2(self):
    sentence = "Hello world."
    with self.assertRaises(TypeError):
      sentence.split(" ")


  
  
if __name__ == "__main__":
  unittest.main()