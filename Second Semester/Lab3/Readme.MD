# Звіт до лабораторної роботи

## Тема: CI/CD автоматизація через GitHub Actions

### Мета роботи:
- Ознайомитися з основами безперервної інтеграції та доставки (CI/CD).
- Навчитися створювати та налаштовувати GitHub Actions workflow.
- Реалізувати автоматичну перевірку коду та юніт-тести.
- Додати запуск workflow вручну та за розкладом (cron).
- Інтегрувати проєкт з Codecov для аналізу покриття тестами.
- Додати бейдж покриття у файл `README.md`.
- Підготувати звіт з демонстрацією роботи CI/CD процесу.

---

## Виконання роботи

### 1. Створення структури
- Створено базову структуру з файлів:
  - `main.py` — основний скрипт з простою логікою (наприклад, калькулятор).
  - `test_main.py` — тести для `main.py`.
  - `.github/workflows/python-app.yml` — workflow-файл для GitHub Actions.
  - `README.md` — опис проєкту з бейджем покриття.

---

### 2. Налаштування GitHub Actions

- **Файл:** `.github/workflows/python-app.yml`  
- **Зміст:**
  - Workflow запускається у трьох випадках: при пуші, pull request, а також вручну (`workflow_dispatch`) і за розкладом (`schedule`).
  - Дії:
    - Встановлення Python.
    - Встановлення залежностей.
    - Запуск тестів.
    - Генерація звіту покриття для Codecov.

```yaml
name: Python CI

on:
  push:
  pull_request:
  workflow_dispatch:
  schedule:
    - cron: '0 12 * * 1'  # кожного понеділка о 12:00

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest pytest-cov codecov
      - name: Run tests
        run: |
          pytest --cov=.
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
```

---

### 3. Тестування проєкту

- **Файл:** `main.py`

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

- **Файл:** `test_main.py`

```python
from main import add, subtract

def test_add():
    assert add(3, 4) == 7

def test_subtract():
    assert subtract(10, 5) == 5
```

- **Результат запуску:**
  Усі тести пройшли успішно.

---

### 4. Додавання бейджа в README

- **Файл:** `README.md`

# CI/CD Lab

[![Python CI](https://github.com/OlenaMizerak/College/actions/workflows/python-app.yml/badge.svg)](https://github.com/OlenaMizerak/College/actions/workflows/python-app.yml)


✅ Бейдж з’явився на головній сторінці репо.

---

## Висновки:

- Налаштовано повноцінний процес CI/CD через GitHub Actions.
- Автоматизовано запуск тестів та збір покриття коду.
- Реалізовано запуск вручну, при push/pull request та по розкладу.
- Інтегровано з Codecov для візуалізації покриття тестами.
- Всі етапи були успішно протестовані та задокументовані у цьому звіті.