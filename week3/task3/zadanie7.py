#7) Определить количество разрядов числа
#Написать функцию, которая определяет количество разрядов введенного целого
#числа
"""def digits(n):
    i = 0
    while n > 0:
        n = n//10
        i += 1
    return i
 
num = abs(int(input('Введите число: ')))
print('Количество разрядов:', digits(num))"""


def func():
    try:
        vvod = int(input("введите число:"))
        vvod2 = str(vvod)
        print(len(vvod2))
    except  Exception:
        print("введите только числа: ")
        func()

func()