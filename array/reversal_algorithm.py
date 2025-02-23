# # a = [4, 5, -1]
# # len_a = len(a)
# # n = int(len_a/ 2)
# # for left in range(n):
# #     right = len_a - left -1
# #     print(left, right)
# #     temp = a[left]
# #     a[left] = a[right]
# #     a[right] = temp
# #     print(a)
# #
# #
#
# # nums = [-1,-100,3,99]
#
#
# # 3, 99, -1, -100
#
# nums = [1,2,3,4,5,6,7]
# k = 2
# len_nums = len(nums)
#
# def reverse(arr, start, end, constant):
#     len_a = len(arr[start:end])
#     n = int(len_a/ 2)
#     for _ in range(n):
#         left = _ + constant
#         right = end - _
#         temp = arr[left]
#         arr[left] = arr[right]
#         arr[right] = temp
#     return arr
#
#
# # section_a = nums[:len_nums-k]
# # section_b = nums[len_nums-k:len_nums]
#
#
#
#
# print(nums)
# nums = reverse(nums, 0, len_nums-k, constant=0)
# nums = reverse(nums, len_nums-k, len_nums, constant=len_nums-k)
# print(nums)



# for k in range(2):
#     pass


# # o/p: 5, 6, 7, 1, 2, 3, 4
#
# nums1 = [1,2,3,4]
# nums2 = [5,6,7]
# # reverse nums2 - [7, 6, 5]
# # reverse nums1 - [4, 3, 2, 1]
# # reverse -  a nd b - 4, 3, 2, 1, 7, 6, 5
# # data: 5, 6, 7, 1, 2, 3, 4


def reversal_algo(arr, start, end, constant):
    len_a = len(arr[start:end])
    n = int(len_a/ 2)
    for _ in range(n):
        left = _ + constant
        right = end - _ - 1
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
    return arr


nums = [1,2,3,4,5,6,7, 8]
k = 3
len_nums = len(nums)

nums = reversal_algo(nums, 0, len_nums-k, 0)
print(nums)
nums = reversal_algo(nums, len_nums-k, len_nums, 5)
print(nums)
nums = reversal_algo(nums,  0, len_nums, 0)
print(nums)


