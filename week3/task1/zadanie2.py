# 2) Написать скрипт, который меняет каждое число на квадрат данного числа
# Пример:
# [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] - до
# #[[1, 4, 9, 16], [25, 36, 49, 64], [81, 100, 121, 144]] - после
# Требование:
# Использовать list comprehension
# Подсказка:
# Nested list comprehension

list = [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]

list2 = [[x**2 for x in y] for y in list]
print(list2)