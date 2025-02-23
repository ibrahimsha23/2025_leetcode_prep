data = "hello_world_14_06"
def reverse(data):
    if not data:
        return ""
    return reverse(data[1:]) + data[0]


def print_reverse(data):
    if not data:
        return ""
    print(data[-1])
    return print_reverse(data[1:])


result = print_reverse(data)
print(result)