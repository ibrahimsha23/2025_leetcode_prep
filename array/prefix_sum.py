array = [1, 2, 3, 4, 5, 6]
# o/p: 1, 3, 6, 10, 15, 21
new = []

for index, i in enumerate(array):
    x = i
    y = new[index-1] if index != 0 else 0
    sum =  x + y
    new.append(sum)
print(new)


