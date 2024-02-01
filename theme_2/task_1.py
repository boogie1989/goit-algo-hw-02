from queue import Queue
import time
import random

# Створення черги заявок
requests_queue = Queue()


def generate_request():
    """Функція для генерації нової заявки."""
    request_id = random.randint(1, 1000)  # Генеруємо унікальний ID для заявки
    print(f"Генеруємо нову заявку з ID: {request_id}")
    requests_queue.put(request_id)  # Додаємо заявку до черги


def process_request():
    """Функція для обробки заявки з черги."""
    if not requests_queue.empty():
        request_id = requests_queue.get()  # Видаляємо заявку з черги
        print(f"Обробляємо заявку з ID: {request_id}")
    else:
        print("Черга пуста")


def main_loop():
    """Головний цикл програми для імітації роботи сервісного центру."""
    try:
        while True:
            generate_request()  # Генеруємо нові заявки
            process_request()  # Обробляємо заявки
            time.sleep(1)  # Чекаємо 1 секунду перед наступною ітерацією
    except KeyboardInterrupt:
        print("Програма завершена користувачем")


main_loop()
