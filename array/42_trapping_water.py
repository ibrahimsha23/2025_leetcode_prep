class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        trapped_water = 0
        len_ht = len(height)

        for i in range(1, len_ht-1):
            left_max = max([height[j] for j in range(0, i)])
            right_max = max([height[k] for k in range(i, len_ht)])

            water_level = min(left_max, right_max)
            ht_block = height[i]

            trapped_water += water_level - ht_block if water_level > ht_block else 0
        return trapped_water


if __name__ == "__main__":
    height = [4,2,0,3,2,5]
    sol = Solution()
    sol.trap(height)
