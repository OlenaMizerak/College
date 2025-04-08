# Файл з класами для валідації введених даних

# Клас для перевірки фігури
class Figure:
    def __init__(self, shape, length):
        # Перевірка типу фігури
        assert shape in ['circle', 'square', 'triangle'], "Невірна фігура"
        self.shape = shape
        
        # Перевірка довжини
        assert isinstance(length, (int, float)) and length > 0, "Довжина повинна бути позитивним числом"
        self.length = length

    def get_shape(self):
        return self.shape

    def get_length(self):
        return self.length


# Клас для перевірки імені та хобі
class Name:
    def __init__(self, name, hobby):
        # Перевірка імені
        self.allowed_names = ['Alice', 'Bob', 'Charlie']
        assert name in self.allowed_names, "Ім'я не в списку дозволених"
        
        # Перевірка хобі
        assert hobby != "", "Хобі не може бути порожнім"
        
        self.name = name
        self.hobby = hobby

    def get_name(self):
        return self.name

    def get_hobby(self):
        return self.hobby
