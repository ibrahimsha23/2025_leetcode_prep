from copy import deepcopy


array_str = "ABC"
len_array = len(array_str)
col_len = int(len_array/2) + 5
col = 0
counter = 0
row = 1
result = ""
col = 0

array = []

for k in range(row):
    array.append([])
    for kl in range(col_len):
        array[k].append(0)


while counter < len_array:
    for i in range(0, row):
        print(counter)
        if counter > len_array-1:
            break;
        # print(i, col, counter)
        array[i][col] = array_str[counter]
        counter += 1

    print("===================================")

    for j in range(row-2, 0, -1):
        print(counter)
        if counter > len_array-1:
            break;
        col += 1
        # print(j, col, counter)
        array[j][col] = array_str[counter]
        counter += 1
    col += 1

    print("************************************")

for i in range(row):
    for j in array[i]:
        if not j == 0:
            result += j


print(result)