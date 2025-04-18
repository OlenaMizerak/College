import unittest
from main import find_max

class TestFindMax(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_max([1, 5, 3, 9, 2]), 9)

    def test_negative_numbers(self):
        self.assertEqual(find_max([-10, -20, -3, -1]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(find_max([-5, 0, 10, 7]), 10)

    def test_single_element(self):
        self.assertEqual(find_max([42]), 42)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            find_max([])

if __name__ == "__main__":
    unittest.main()
