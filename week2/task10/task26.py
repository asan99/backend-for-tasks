
list_ = [7, 6, 5, 4, 3, 2, 1, 2]
print("Введите index:")
k = int(input())

for num in range(len(list_)-1) :
    if k == list_[num]:
        list_.pop(list_[num])
for num in range(len(list_)-1) :
    if k == 0:
        list_.pop(0)
        break
list_.pop()
print(list_)
