import unittest
from random import choice, randint
from app import Figure
  
class TestFigure(unittest.TestCase):
      @classmethod
      def setUpClass(cls):
          """Виконається лише раз на початку тестів"""
          pass
  
      def setUp(self) -> None:
          """Виконується перед кожним тестом"""
          self.figure = choice(Figure.FIGURES)
          self.length = randint(1, 10)
          self.obj = Figure(self.figure, self.length)
          return super().setUp()
  
      def tearDown(self) -> None:
          del self.obj
          return super().tearDown()
  
      def test_figure_type(self):
          print(f"Тестуємо вивід: {self.figure} == {self.obj.get_figure_type}")
          self.assertEqual(self.figure, self.obj.get_figure_type, "Властивість get_figure_type повертає неправильну фігуру!")
  
      def test_figure_length(self):
          self.assertEqual(self.length, self.obj.get_figure_length, "Властивість get_figure_length повертає неправильну довжину!")
      
      def test_obj_invalid(self):
          with self.assertRaises(AssertionError):
              Figure("коло", 1)
  
if __name__ == '__main__':
      unittest.main(verbosity=2)