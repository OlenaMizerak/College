def find_max(numbers: list[int]) -> int:
    if not numbers:
        raise ValueError("Список не може бути порожнім")
    return max(numbers)

if __name__ == "__main__":
    user_input = input("Введіть числа через пробіл: ")
    numbers = list(map(int, user_input.strip().split()))
    print("Максимальне число:", find_max(numbers))
