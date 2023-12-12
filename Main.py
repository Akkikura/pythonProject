import openpyxl
from math import *
from count_characters import *

with open('data.txt', 'r', encoding='utf-8') as file:
    text = file.read()
characters = '0123456789абвгдеёжзийклмнопрстуфхцчшщъыьэюя.,:;- ('
result = count_characters(text, characters)
special_symbols = '.,:;- ('
entropy = {}
print("Результат подсчета:")
for char, character_count in result.items():
    print(f"Символ '{char}': {character_count} раз(а)")
text_chars = sum(result.values())
for i in result.keys():
    entropy[i] = result[i] / text_chars
for char, character_count in entropy.items():
    print(f"Энтропия '{char}': {character_count} единиц")
P = sum(entropy.values())
print(f'Всего в тексте {text_chars} символов')
print(f'Полная вероятность в тексте = {P}')
H = 0
Ismall = {}
for i in result.keys():
    if entropy[i] > 0:
        Ismall[i] = (-1) * log2(entropy[i])
    else:
        Ismall[i] = 0
    print(f'Ismall для {i} равняется {Ismall[i]}')
    H += Ismall[i]*entropy[i]
print(f'Полная энтропия равна {H}')
