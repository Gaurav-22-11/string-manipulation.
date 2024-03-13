import unittest
from string_manipulation import StringManipulation

class TestStringManipulation(unittest.TestCase):
  def setUp():
    self.bot=StringManipulation()

  def test_concatenate(self):
    result=self.bot.concatenate("Hello","World")
    self.assertEqual(result, "Hello World")

  def test_uppercase_conversion(self):
    result= self.bot.convert_to_upper("hello")
    self.assertEqual(result,"HELLO")

  def test_substring_extraction(self):
    result= self.bot.extract_substring("Hello","World!",7,12)
    self.assertEqual(result, "World")

if __name__ == '__main__':
  unittest.main()
