class Figure:
      FIGURES = ["квадрат", "прямокутник", "трикутник"]
      
      def __init__(self, type, length) -> None:
          assert length > 0, "Довжина має бути більшою за 0!"
          assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
          self.type = type
          self.length = length
  
      @property
      def get_figure_type(self):
          return self.type
  
      @property
      def get_figure_length(self):
          # Намірено зроблено помилку (повертаємо type замість length)
          return self.type
  
      @property
      def get_angles(self):
          if self.type in ["квадрат", "прямокутник"]:
              return 4
          if self.type == "трикутник":
              return 3
  
  # Приклад використання класу
if __name__ == '__main__':
      fig = Figure("квадрат", 5)
      print(f"Тип фігури: {fig.get_figure_type}")
      print(f"Довжина: {fig.get_figure_length}")
      print(f"Кількість кутів: {fig.get_angles}")

# Додаємо тестову функцію для PyTest
def test_app_triangle():
    """Test if we create triangle figure."""
    fig = "трикутник"
    triangle = Figure(fig, 4)
    assert triangle.get_figure_type == fig, f"Фігура має бути {fig}"
