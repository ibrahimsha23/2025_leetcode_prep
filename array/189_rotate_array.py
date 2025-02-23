nums = [-1, -100, 3, 99]
k = 2
i =1
nums_len = len(nums)
print(nums)
while i <= k:
    x = nums[nums_len-1]
    j = 1
    while j < nums_len:
        nums[nums_len-j] = nums[nums_len-j-1]
        j += 1
    nums[0] = x
    print(nums)
    i += 1


