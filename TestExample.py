import unittest


class TestExample(unittest.TestCase):
    def test_addition(self):
        result = 2 + 2  # 2 + 3 => AssertionError: 5 != 4
        self.assertEqual(result, 4)

# In summary, an AssertionError is an exception that is raised when an assertion fails in your code.
