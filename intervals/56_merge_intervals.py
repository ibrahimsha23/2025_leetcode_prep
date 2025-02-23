class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        merged = []
        merge_cursor = 0
        intervals.sort(key=lambda x: x[0])
        len_interval = len(intervals)
        if len_interval == 0:
            return merged
        else:
            merge_cursor += 1
            merged.append(intervals[0])

        for i in range(1, len_interval):
            merged_pointer = merged[merge_cursor - 1]
            if merged_pointer[1] >= intervals[i][1]:
                continue
            elif merged_pointer[1] >= intervals[i][0]:
                merged_pointer = [merged_pointer[0], intervals[i][1]]
                merged[merge_cursor-1] = merged_pointer
            else:
                merged_pointer = intervals[i]
                merged.append(merged_pointer)
        return merged

if __name__ == "__main__":
    intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]

    sol = Solution()
    sol.merge(intervals)
