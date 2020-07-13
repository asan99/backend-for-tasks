# Три ввода и сверьте их, все ли равны или что-либо из них?

print("Введите 1-ое значение")
user1 = (input())
print("ВВедите 2-ое значение")
user2 = (input())
print("ВВедите 3-ee значение")
user3 = (input())
if user1 == user2 == user3:
    print("Все значения равны")
elif user1 == user2 or user1 == user3:
    print("Два из этих значений равны")
elif user2 == user1 or user2 == user3:
    print("Два из этих значений равны")
elif user3 == user1 or user3 == user2: 
    print("Два из этих значений равны")
else:
    print ("Ничего не равно")