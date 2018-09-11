import unittest
from vowels import vowels
class Vowels(unittest.TestCase):
     """
        This tests methods in vowels file
     """
     def test_missing_elements(self):
         self.assertEqual(('a',3), vowels.vowels(["dahdah"]),msg='The output should be an instance of vowels')


if __name__ == "__main__":
    unittest.main()