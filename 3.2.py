"""
Часто встречающиеся слова

Пример

На входе:

text = 'Hello world. Hello Python. Hello again.'
На выходе:

[('hello', 3), ('world', 1), ('python', 1), ('again', 1)]
"""

text = 'Hello world. Hello Python. Hello again.'

# Введите ваше решение ниже
import re
from collections import Counter

# Удаляем знаки препинания и приводим текст к нижнему регистру
cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# Разбиваем текст на слова и считаем их количество
words = cleaned_text.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Получаем 10 самых часто встречающихся слов
top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

print(top_words)