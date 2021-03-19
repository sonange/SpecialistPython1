# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке

def palindrome(number):
    number_to_str = str(number)
    rem_2 = len(number_to_str) % 2
    middle_index = len(number_to_str) // 2
    if number_to_str[:middle_index + 1 * rem_2] == number_to_str[:middle_index - 1:-1]:
        return True
    else:
        return False


# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
