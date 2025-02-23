# nums = [0,0,1,1,1,2,2,3,3,4]
nums = [0,0,1,1,1,1,2,3,3]

# nums = [1, 1, 1, 2, 2, 3]

n = len(nums)
largest_cursor, i = 0, 1
occured = 1

for i in range(1, n):

    if nums[i] ==  nums[largest_cursor] and occured < 2:
        occured += 1
        largest_cursor += 1
        nums[largest_cursor] = nums[i]
    elif nums[i] > nums[largest_cursor]:
        occured = 1
        largest_cursor += 1
        nums[largest_cursor] = nums[i]
    print(nums)
print("largest_cursor = {largest_cursor}".format(largest_cursor=largest_cursor+1))

