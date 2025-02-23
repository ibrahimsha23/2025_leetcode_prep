nums = [2,3,1,1,4]


def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    l, r = 0, 0
    counter = 0
    target = len(nums) - 1
    while r < target:
        counter += 1
        max_val = 0
        for i in range(l, r + 1):
            max_val = max(max_val, nums[i]+i)
        l = r + 1
        r = max_val
    return counter

jump(nums)