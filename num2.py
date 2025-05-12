import re

def is_palindrome(input_string: str) -> bool:
    """Проверяет, является ли строка палиндромом (игнорирует регистр и не-буквенные символы)"""
    normalized_text = re.sub(r'[^\wа-яёА-ЯЁ]', '', input_string.lower())
    return normalized_text == normalized_text[::-1]

# Тесты
assert is_palindrome("топот") == True
assert is_palindrome("А роза упала на лапу Азора!") == True
assert is_palindrome("Привет, мир!") == False
assert is_palindrome("LeV3l") == False  
assert is_palindrome("") == True
assert is_palindrome("Лёша на полке клопа нашёл") == True
assert is_palindrome("Я") == True

print("Все тесты прошли успешно!")