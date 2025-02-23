s = "race a car"

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
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    6: True,
    7: True,
    8: True,
    9: True,
    0: True,
}

def isPalindrome(s, data):
    is_pali = False
    len_s = len(s)

    i =0
    j = len_s - 1

    while i < j:
        print(s[i], s[j])
        left = data.get(s[i].lower(), None)
        right = data.get(s[j].lower(), None)

        if not left:
            i += 1
        elif not right:
            j -= 1
        elif s[i].lower() == s[j].lower():
            i += 1
            j -= 1
        else:
            break


    return is_pali







if __name__ == "__main__":
    isPalindrome(s, data)