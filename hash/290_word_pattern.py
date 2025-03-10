class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        split_word = s.split(' ')
        print(len(pattern), len(split_word), split_word)
        if len(pattern) != len(split_word):
            return False

        char_to_word_mapper = {}

        for i in range(len(pattern)):
            if pattern[i] not in char_to_word_mapper:
                char_to_word_mapper[s[i]] = split_word[i]
            elif char_to_word_mapper[pattern[i]] == split_word[i]:
                continue
            else:
                return False
        return True

# pattern, s = "abba", "dog cat cat dog"
# pattern, s = "abba", "dog cat cat fish"
# pattern, s = "aaaa", "dog cat cat dog"
pattern, s = "abba", "dog dog dog dog"
sol = Solution().wordPattern(pattern, s)