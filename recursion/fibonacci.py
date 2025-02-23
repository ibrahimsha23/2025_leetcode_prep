"""
Recursion: a function call by itself
"""

def fb(n):
    print(n)
    if n == 1 or n == 0:
        return n
    return fb(n-1) + fb(n-2)

result = fb(10)
print(result)