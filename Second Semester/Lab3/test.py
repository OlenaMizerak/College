import unittest
from app import Figure

class TestFigure(unittest.TestCase):
    
    def test_shape(self):
        figure = Figure('circle', 5)
        self.assertEqual(figure.get_shape(), 'circle')
    
    def test_length(self):
        figure = Figure('circle', 5)
        self.assertEqual(figure.get_length(), 5)

    def test_invalid_shape(self):
        with self.assertRaises(ValueError):
            Figure('hexagon', 5)

    def test_invalid_length(self):
        # Перевірка, що AssertionError з'являється при неправильній довжині
        with self.assertRaises(AssertionError):
            Figure('square', -3)

if __name__ == '__main__':
    unittest.main()
