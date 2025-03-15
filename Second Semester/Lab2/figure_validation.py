class Figure:
      def __init__(self, type, length) -> None:
          assert length > 0, "Довжина має бути більшою за 0!"
          assert type in ["квадрат", "прямокутник", "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"
          self.type = type
          self.length = length
  
  # Приклади створення об'єктів:
  # a = Figure("трапеція", 12)
  # b = Figure("квадрат", 0)
c = Figure("квадрат", 1)
  
  
class Name:
      def __init__(self, name, hobby) -> None:
          if name not in ["Богдан", "Анонім", "Олена"]:
              raise ValueError("Дозволені імена: Богдан, Анонім, Олена")
          if not hobby:
              raise ValueError("Хоббі не може бути порожнім!")
          self.name = name
          self.hobby = hobby
  
  # Приклад створення об'єкта:
  # a = Name("Бодько", "читання")
a = Name("Олена", "програмування")
print(f"Ім'я: {a.name}, Хоббі: {a.hobby}")