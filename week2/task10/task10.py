def divide(array):
    positive = []
    negative = []
    for i in array:
        if i > 0:
            positive.append(i)
        elif i < 0:
            negative.append(i)
    return positive, negative
 
 
arr = [1, 2, 3, -1, -2, -3]
pos, neg = divide(arr)
print(pos)
print(neg)