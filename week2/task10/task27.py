nums = [1,2, 3, 4, 5, 6, 7]
lst = nums
steps = -6
if steps < 0:
    steps = abs(steps)
    for i in range(steps):
        lst.append(lst.pop(0))
else:
    for i in range(steps):
        lst.insert(0, lst.pop())
lst = nums
print(nums)
18