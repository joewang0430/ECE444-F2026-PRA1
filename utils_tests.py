import unittest # the built-in tool for testing in Python
from utils import utils # import the class from the file

# the class TestUtils is inheritted from the class unittest.TestCase
class TestUtils(unittest.TestCase):

    def setUp(self):
        self.utils = utils()    # create a utils object

    def test_reversed_integer(self):
        self.assertEqual(self.utils.reversed(1234), 4321) # assert if equal

    # As defined in utils.py, I give errors when the type is not int.
    # with: check if a certain line of code report a specified error
    def test_reversed_string(self):
        with self.assertRaises(TypeError):
            self.utils.reversed("1234")

    def test_reversed_float(self):
        with self.assertRaises(TypeError):
            self.utils.reversed(123.45)

    def test_formatter_integer(self):
        self.assertEqual(self.utils.formatter(10), ("0b1010", "0o12"))

    def test_formatter_string(self):
        with self.assertRaises(TypeError):
            self.utils.formatter("10")

    def test_formatter_float(self):
        with self.assertRaises(TypeError):
            self.utils.formatter(10.5)


if __name__ == "__main__":
    unittest.main() # unittest.main(): autoly finds all test_... and excecutes