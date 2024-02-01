from collections import deque


def is_palindrome(s):
    # Підготовка рядка: видалення пробілів та перетворення на нижній регістр
    cleaned_str = ''.join(s.split()).lower()

    # Створення двосторонньої черги з символів рядка
    char_deque = deque(cleaned_str)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True


# Тестування функції
test_strings = ["A man a plan a canal Panama",
                "Madam In Eden I'm Adam", "Not a palindrome"]
for test_str in test_strings:
    print(f"\"{test_str}\" - це паліндром? {is_palindrome(test_str)}")
