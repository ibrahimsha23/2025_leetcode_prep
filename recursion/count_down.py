
def cd(n):
    print(n)
    if n == 0:
        return n
    return cd(n-1)
cd(4)