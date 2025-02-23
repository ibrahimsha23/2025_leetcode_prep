a = "0P"

data = {
    'a': True,
    'b': True,
    'c': True,
    'd': True,
    'e': True,
    'f': True,
    'g': True,
    'h': True,
    'i': True,
    'j': True,
    'k': True,
    'l': True,
    'm': True,
    'n': True,
    'o': True,
    'p': True,
    'q': True,
    'r': True,
    's': True,
    't': True,
    'u': True,
    'v': True,
    'w': True,
    'x': True,
    'y': True,
    'z': True,
    '1': True,
    '2': True,
    '3': True,
    '4': True,
    '5': True,
    '6': True,
    '7': True,
    '8': True,
    '9': True,
    '0': True,
}

result = ''

for i in a:
    if data.get(i.lower()):
        result += i.lower()


result_len = len(result)

is_even = True if result_len % 2 == 0 else False

# ((result_len//2) + 1)
output = True
i = 0
j = result_len -1
while i < result_len//2:
    if result[i] != result[j]:
        output = False
        break
    i += 1
    j -= 1

print(result, result_len)
print(output)