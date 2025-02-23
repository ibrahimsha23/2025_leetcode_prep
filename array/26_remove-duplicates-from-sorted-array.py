nums = [0,0,1,1,1,2,2,3,3,4]

n = len(nums)
largest_cursor, i = 0, 1
while i < n:
    if nums[largest_cursor] < nums[i]:
        largest_cursor += 1
        nums[largest_cursor] = nums[i]
    else:
        i += 1
print(largest_cursor)
print(nums)

