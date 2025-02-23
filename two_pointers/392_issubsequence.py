class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # sub_string_count = 0
        # for i in s:
        #     for j in t:
        #         if i == j:
        #             sub_string_count += 1
        #             break
        # return True if sub_string_count == len(s) else False

        sub_string_count = 0
        len_sub_str = len(s)
        for j in t:
            print()
            if sub_string_count < len_sub_str and s[sub_string_count] == j:
                sub_string_count += 1
        return True if sub_string_count == len_sub_str else False

if __name__ == "__main__":
    sol = Solution()
    s = "abc"
    t = "ahbgdc"
    print(sol.isSubsequence(s, t))