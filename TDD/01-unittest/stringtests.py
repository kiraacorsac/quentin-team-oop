import unittest

class String(unittest.TestCase):
    def setUp(self):
        self.simpleSentence = "hello world"

    def test_upper_simple_makesUppercase(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper_upper_true(self):
        self.assertTrue('FOO'.isupper())

    def test_isupper_upper_false(self):
        self.assertFalse('Foo'.isupper())

    def test_split_simpleSentence_splits(self):
        self.assertEqual(self.simpleSentence.split(" "), ['hello', 'world'])

    def test_split_numberSeparator_raises1(self):
        # check that s.split fails when the separator is not a string
        try:
            self.simpleSentence.split(2)
        except TypeError:
            return
        self.fail()

    def test_split_numberSeparator_raises2(self):
        sentence = 'hello world'
        with self.assertRaises(TypeError):
            sentence.split(2)

    def test_split_longSentence_longList(self):
      sentence = 'hello world how are we doing today, this is a lot of words'
      self.assertGreater(len(sentence.split(" ")), 5)
      #self.assertLesser exists too

    def test_split_longSentence_containsWord(self):
      sentence = 'hello world how are we doing today, this is a lot of words'
      self.assertIn("doing", sentence.split(" "))

    def test_float_similiarNumbers_almostEqual(self):
      self.assertAlmostEqual(0.334, 0.333, 2)
      #show that these test can be rewritten with asserEqual!

    # to control what to do with your tests

    @unittest.skip("Broken!")
    def test_fail_fails(self):
      self.fail()

    # use this decorator when your test is broken and you can't fix it yet,
    # not when you want to 'flip' the result!
    @unittest.expectedFailure
    def test_assertFalse_True_Fails(self): 
        self.assertFalse(True)


if __name__ == '__main__':
    unittest.main()
