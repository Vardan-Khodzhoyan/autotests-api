import time
# Создаем генератор случайного email
def get_random_email() -> str:
    return f"test.{time.time()}@example.ru"