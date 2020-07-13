# 1) Написать генератор списка, который итерируется по функции range от 1 до 100
# и фильтрует по четным числам.
# Пример:
# [1, 2, 3, 4, 5, 6]
# [2, 4, 6]
# Требование:
# Использовать list comprehension

spisok = range(1,101)
spisok2 = [num for num in spisok if num %2 == 0]
print(spisok2)