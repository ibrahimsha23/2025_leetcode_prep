class Solution(object):
    a = 5

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        k = m + n

        print("Initial nums1:", nums1)
        print(Solution.a)

        while m > 0 and n > 0:
            print("At m={m}, n={n}, k={k}".format(m=m, n=n, k=k))

            if nums1[m - 1] > nums2[n - 1]:
                nums1[k - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[k - 1] = nums2[n - 1]
                n -= 1

            k -= 1
            print("nums1:", nums1)

        while not m > 0 and n > 0:
            print("nums2 loop:", nums1, m, n, k)
            nums1[k - 1] = nums2[n - 1]
            n -= 1
            k -= 1
            print("nums2 post loop:", nums1, m, n, k)


if __name__ == "__main__":
    nums1 = [4,5,6,0,0,0]
    nums2 = [1, 2, 3]
    m = 3
    n = 3

    sol = Solution()
    sol.merge(nums1, m, nums2, n)
