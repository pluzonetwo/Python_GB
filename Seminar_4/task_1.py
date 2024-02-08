# Задание №1 Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

input_text = input('Input string: ')

def func(text):
    text = sorted(text.split())
    max_length = len(max(text, key=len))
    for i, value in enumerate(text, 1):
        print(f'{i}. {value:>{max_length}}')
    return text

func(input_text)