class Solution(object):
    def merge(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        merged = []
        merge_cursor = 0
        intervals.append(newInterval)
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
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]

    sol = Solution()
    sol.merge(intervals)
