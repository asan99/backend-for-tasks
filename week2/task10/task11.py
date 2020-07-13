numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)

for index, lis in enumerate(numbers, 0):
    if index %2 == 0:
        print(index, lis)