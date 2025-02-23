s = "EPY2giL"
result = ""
temp = ""
len_data = len(s)
last_char = False

for i in range(len_data-1, -1, -1):
    x = s[i]

    if x == " " and temp:
        # result.append(temp)
        result = result + x + temp if result else temp
        temp = ''
    else:
        temp = x + temp

if temp:
    # result.append(temp)
    # result = result + x + temp if result else temp
    result = temp + (" " + result if result else "")

# c
print(len_data, result, len_data)
print(len(result))
