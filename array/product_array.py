nums = [1,2,3,4]

prefix_nums = []
result = []
kdx = len(nums)
postfix_nums = [0] * kdx


print(postfix_nums)

for idx in range(len(nums)):
    kdx -= 1
    last_transaction_idx = idx-1
    last_transaction_kdx = kdx + 1

    print(kdx, idx)

    if idx == 0:
        prefix_nums.append(1)
    else:
        data = prefix_nums[last_transaction_idx] * nums[last_transaction_idx]
        prefix_nums.append(data)

    if kdx == len(nums)-1:
        postfix_nums[kdx] = 1
    else:
        postfix_nums[kdx] = postfix_nums[last_transaction_kdx] * nums[last_transaction_kdx]


    # print(prefix_nums)
for idx in range(len(nums)):
    result.append(prefix_nums[idx] * postfix_nums[idx])
print(result)

