import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # nums = sorted(nums, reverse=True)
        # print(nums)
        # return nums[k-1]
        data = []
        for ele in nums:
            print("length of data is ", len(data))
            if len(data) < k :
                heapq.heappush(data, ele)
            else:
                heapq.heappush(data, ele)
                heapq.heappop(data)
            print(data)

        return heapq.heappop(data)

nums = [3,2,1,5,6,4]
k = 2
sol = Solution()
min_val = sol.findKthLargest(nums, k)
print(min_val)
