"""
Recursion: a function call by itself
"""

def fac(n):
    if n == 1:
        return n
    return n * fac(n-1)

result = fac(10)
print(result)