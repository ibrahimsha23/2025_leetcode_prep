nums = 3749
nums_str = str(nums)

array = []
while nums > 9:
    divider = str(nums)
    answer = divmod(
        nums,
        pow(10, len(divider)-1)
    )
    array.append(answer[0]*pow(10, len(divider)-1))
    nums = answer[1]

if nums > 0:
    array.append(nums)


hash_map = [1000, 500, 100, 50, 10, 5, 1]

data_map = {
    0: 'M',
    1: 'D',
    2: 'C',
    3: 'L',
    4: 'X',
    5: 'V',
    6: 'I',
}

for i in array:

    if i >= hash_map[0]:
        pass
    elif i >= hash_map[1]:
        pass
    elif i >= hash_map[2]:
        pass
    elif i >= hash_map[3]:
        pass
    elif i >= hash_map[4]:
        pass
    elif i >= hash_map[5]:
        pass
    elif i >= hash_map[6]:
        pass



print(array)

