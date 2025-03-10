class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        def multiply(a, b):
            return a * b

        def sum_fun(a, b):
            return a + b

        def min_fun(a, b):
            return a - b

        def div(a, b):
            print(a, "/", b)
            result = int(a / b) if a >= b else 0
            print(result)
            return result

        hash_table = {
            "*": multiply,
            "+": sum_fun,
            "/": div,
            "-": min_fun,
        }
        stack = []
        n = len(tokens)
        i = 0
        while i < n:
            token = tokens[i]

            if token in hash_table:
                last_ele = stack.pop(-1)
                first_ele = stack.pop(-1)
                result = hash_table[token](first_ele, last_ele)
                stack.append(result)
            else:
                stack.append(int(token))
            print(stack)
            i += 1
        return stack.pop(0)

# tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
tokens = ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]
sol = Solution()
r = sol.evalRPN(tokens)
print(r)


