import unittest


class StringTest(unittest.TestCase):
  def setUp(self):
    self.simple_sentence = "Hello world."
    self.long_sentence = 'hello world how are we doing today'
    self.testfile = open("testfile.txt", "w")

  def tearDown(self):
    self.testfile.close()

  # test_what_when_expected
  def test_upper_simpleSentence_UPPER(self):
    self.assertEqual(self.simple_sentence.upper(), "HELLO WORLD.")

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
    self.assertEqual(self.simple_sentence.split(" "), ['Hello', "world."])

  def test_split_simpleSentenceOnNumber_raises(self):
    try:
      self.simple_sentence.split(2)
    except TypeError:
      return
    self.fail("Splitting on 2 should result in an exception")

  def test_split_simpleSentenceOnNumber_raises2(self):
    with self.assertRaises(TypeError):
      self.simple_sentence.split(2)

  def test_split_longSentence_containsWord(self):
    self.assertIn("doing", self.long_sentence.split(" "))
  
  def test_count_longSentence_bigEnough(self):
    self.assertGreater(self.long_sentence.count('o'), 4)
    # self.assertTrue(long_sentence.count('o') > 10)

  def test_float_similiarNumbers_almostEqual(self):
    self.assertAlmostEqual(0.334, 0.333, 2)

  def test_write_fileWriting_notRaises(self):
    self.testfile.write("Hello world!")
  
  @unittest.skip("Broken!")
  def test_split_longSentence_containsWordError(self):
    self.assertIn("error", self.long_sentence.split(" "))
  
  @unittest.expectedFailure
  def test_split_longSentence_containsWordError2(self):
    self.assertIn("world", self.long_sentence.split(" "))
  
if __name__ == "__main__":
  unittest.main()