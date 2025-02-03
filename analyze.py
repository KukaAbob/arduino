import json
import re

# Загрузка данных из JSON файла
with open('questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

questions = data['questions']

# Статистика по правильным ответам
answer_stats = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
correct_answer_lengths = []
incorrect_answer_lengths = []

# Статистика по наличию скобок
correct_with_parentheses = 0
incorrect_with_parentheses = 0

# Статистика по вызовам функций
correct_with_function_calls = 0
incorrect_with_function_calls = 0

# Статистика по наличию чисел
correct_with_numbers = 0
incorrect_with_numbers = 0

for question in questions:
    correct_answer = question['correct']
    answer_stats[correct_answer] += 1
    
    # Длина правильного ответа
    correct_answer_text = question['options'][correct_answer]
    correct_answer_length = len(correct_answer_text)
    correct_answer_lengths.append(correct_answer_length)
    
    # Проверка наличия скобок в правильном ответе (исключая вызовы функций)
    if re.search(r'\(.*?\)', correct_answer_text) and not re.search(r'\w+\(.*?\)', correct_answer_text):
        correct_with_parentheses += 1
    
    # Проверка наличия вызова функции в правильном ответе
    if re.search(r'\w+\(.*?\)', correct_answer_text):
        correct_with_function_calls += 1
    
    # Проверка наличия чисел в правильном ответе
    if re.search(r'\d', correct_answer_text):
        correct_with_numbers += 1
    
    # Длины неправильных ответов
    for option, text in question['options'].items():
        if option != correct_answer:
            incorrect_answer_lengths.append(len(text))
            # Проверка наличия скобок в неправильных ответах (исключая вызовы функций)
            if re.search(r'\(.*?\)', text) and not re.search(r'\w+\(.*?\)', text):
                incorrect_with_parentheses += 1
            # Проверка наличия вызова функции в неправильных ответах
            if re.search(r'\w+\(.*?\)', text):
                incorrect_with_function_calls += 1
            # Проверка наличия чисел в неправильных ответах
            if re.search(r'\d', text):
                incorrect_with_numbers += 1

# Средняя длина правильных и неправильных ответов
avg_correct_length = sum(correct_answer_lengths) / len(correct_answer_lengths)
avg_incorrect_length = sum(incorrect_answer_lengths) / len(incorrect_answer_lengths)

# Вывод статистики
print("Статистика по правильным ответам:")
for option, count in answer_stats.items():
    print(f"{option}: {count} раз")

print(f"\nСредняя длина правильных ответов: {avg_correct_length:.2f}")
print(f"Средняя длина неправильных ответов: {avg_incorrect_length:.2f}")

if avg_correct_length > avg_incorrect_length:
    print("\nГипотеза подтверждена: правильные ответы в среднем длиннее.")
else:
    print("\nГипотеза не подтверждена: правильные ответы не длиннее.")

# Вывод статистики по наличию скобок
print(f"\nПравильные ответы со скобками (исключая вызовы функций): {correct_with_parentheses} раз")
print(f"Неправильные ответы со скобками (исключая вызовы функций): {incorrect_with_parentheses} раз")

if correct_with_parentheses > incorrect_with_parentheses:
    print("\nГипотеза подтверждена: правильные ответы чаще содержат скобки.")
else:
    print("\nГипотеза не подтверждена: правильные ответы не чаще содержат скобки.")

# Вывод статистики по вызовам функций
print(f"\nПравильные ответы с вызовами функций: {correct_with_function_calls} раз")
print(f"Неправильные ответы с вызовами функций: {incorrect_with_function_calls} раз")

if correct_with_function_calls > incorrect_with_function_calls:
    print("\nГипотеза подтверждена: правильные ответы чаще содержат вызовы функций.")
else:
    print("\nГипотеза не подтверждена: правильные ответы не чаще содержат вызовы функций.")

# Вывод статистики по наличию чисел
print(f"\nПравильные ответы с числами: {correct_with_numbers} раз")
print(f"Неправильные ответы с числами: {incorrect_with_numbers} раз")

if correct_with_numbers > incorrect_with_numbers:
    print("\nГипотеза подтверждена: правильные ответы чаще содержат числа.")
else:
    print("\nГипотеза не подтверждена: правильные ответы не чаще содержат числа.")