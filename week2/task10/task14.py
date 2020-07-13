numbers = [1, 3, 2, 4, 4, 8, 9, 5, 6, 7]

for lis in range(1, len(numbers)-1):
    string = numbers[lis]
    last_string = numbers[lis-1]
    if numbers[lis-1] < string > numbers[lis+1]:
        print(numbers)