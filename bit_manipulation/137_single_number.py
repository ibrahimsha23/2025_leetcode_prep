

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 3
        output = 0
        for i in nums:
            bin_i = int(bin(i)[2:]) if i >= 0 else int(bin(i)[3:])
            output += bin_i
        output = str(output)
        result = ""
        for i in output:
            mod = int(i) % k
            result += str(mod)

        final_output = int(result, 2)
        print(final_output)


# nums = [2,2,2, 3]
nums = [-2,-2,1,1,4,1,4,4,-4,-2]

for i in nums[::-1]:
    print(i)

# sol = Solution()
# sol.singleNumber(nums)