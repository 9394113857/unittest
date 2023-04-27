import unittest


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(2 + 2, 4)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)

    def test_multiplication(self):
        self.assertEqual(2 * 3, 6)

    def test_division(self):
        with self.assertRaises(ZeroDivisionError):
            2 / 0

    def test_skip(self):
        self.skipTest("Skipping test for demonstration purposes.")

    def test_fail(self):
        self.fail("Intentional failure for demonstration purposes.")

    def test_type_error(self):
        with self.assertRaises(TypeError):
            int('hello')

    def test_value_error(self):
        with self.assertRaises(ValueError):
            int('-10')

    def test_name_error(self):
        with self.assertRaises(NameError):
            print(undefined_variable)
