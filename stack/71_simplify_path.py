# '.' - represents the current directory.
# '..' - represents the previous/parent directory
# '//' and '///' are treated as a single slash '/'.
#  '...' and '....' are valid directory or file names -> > 2 dot


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []

        for i in path.split('/'):
            if i == "..":
                stack.pop() if stack else None
            elif i == "" or i == ".":
                continue
            else:
                stack.append(i)

        data = ''
        for k in stack:
            data += '/' + k
        return data if data else '/'


# path = "/home/"
# path = "/home//foo/"
# path = "/home/user/Documents/../Pictures"
# path = "/../"
# path = "/.../a/../b/c/../d/./"

sol = Solution()
result = sol.simplifyPath(path)

print(result)