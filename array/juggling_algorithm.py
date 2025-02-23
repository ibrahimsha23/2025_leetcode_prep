# nums = [1,2,3,4,5,6,7]
nums = [-1,-100,3,99]

n = len(nums)
k = 2


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


rotation = gcd(n, k)

for k_ele in range(rotation):
    i = 0
    last = nums[i]
    while i < n:
        i += k
        temp = nums[i%n]
        nums[i%n] = last
        last = temp
    print(nums)
