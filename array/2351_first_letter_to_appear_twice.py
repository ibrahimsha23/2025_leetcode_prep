import string



class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        mapper = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
         'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
         'z': 25}
        data = [False] * 26
        for i in s:
            pos = mapper[i]
            if data[pos]:
                return i
            else:
                data[pos] = True
        return None

if __name__ == "__main__":
    s = "abccbaacz"
    sol = Solution()
    x = sol.repeatedCharacter(s)
    print(x)




