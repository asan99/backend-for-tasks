"""2) Напишите программу которая принимает любое число если число четное,
то программа должна сказать ,что это число четное если нет, то сказать ,что оно
нечетное"""

def odd_or_not():
    a = int(input("Введите число:"))
    if a %2 ==0:
        print("Четное")
    else:
        print("Нечетное")    

odd_or_not()