# nums = [2,2,1,1,1,2,2]
nums = [3,2,3]

count = 0
candidate = None

for i in nums:
    if candidate is None:
        candidate = i

    if candidate == i:
        count += 1
    else:
        count -= 1

    if count == 0:
        candidate = i
        count += 1

candidate_occurrence = sum(1 for i in nums if i == candidate)

data = candidate_occurrence > len(nums) // 2

print(data)

