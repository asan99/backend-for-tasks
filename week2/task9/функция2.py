# 2. Напишите программу, которая принимает от пользователя цифру и присваивает его
# переменной given_number. Далее, нужно чтобы было следующее:
# a. если given_number делится на цифру 3 и на цифру 5 без остатков, выведите на
# экран "HahaHoo"
# b. если given_number делится на цифру 3 без остатков, выведите на экран "Haha"
# c. если given_number делится на цифру 5 без остатков, выведите на экран "Hoo"
# d. если given_number не делится без остатков ни на один из вышеуказанных цифр (т.е.
# 3 и 5), то вывести "Aaaaa"
print("Введите число")
given_number = int(input())
if given_number %3 and given_number%5 == 0:
    print("HahaHoo")
elif given_number %3 == 0:
    print("Haha")
elif given_number %5 == 0:
    print("Hoo")
else:
    print("Aaaaa")