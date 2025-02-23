class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # sign_val = '_'
        # counter = 0
        # len_nums = len(nums)
        # i, j = 0, len_nums - 1
        # while j > 0 and i < len_nums:
        #     left_pointer = nums[i]
        #     right_pointer = nums[j]
        #     if left_pointer is val and not left_pointer == sign_val:
        #         counter += 1
        #         if right_pointer is val:
        #             nums[j] = sign_val
        #             j -= 1
        #         else:
        #             nums[i] = nums[j]
        #             nums[j] = sign_val
        #             i += 1
        #             j -= 1
        #     else:
        #         i += 1
        # print(nums)
        # return counter

        # new solution
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n



if __name__ == "__main__":
    # nums = [3, 2, 2, 3]
    # val = 3
    nums = [0, 1, 2, 2, 3, 0, 4, 2]

    val = 2
    sol = Solution()
    sol.removeElement(nums, val)


