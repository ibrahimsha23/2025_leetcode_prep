ascii_range = [97, 122, 26]

def encrypt(msg):
    result = ""
    second_step = 1
    for i in msg:
        ordinal_val = ord(i)
        second_step += ordinal_val
        char_value = second_step
        while char_value > ascii_range[1]:
            char_value -= ascii_range[2]
        result += chr(char_value)
    print(result)

def decrypt(word):
    secondStep = 1
    decryption = ""

    for i in range(len(word)):
        newLetterAscii = ord(word[i])
        newLetterAscii = newLetterAscii - secondStep

        while newLetterAscii < ord('a'):
            newLetterAscii += 26

        decryption += chr(newLetterAscii)
        secondStep += newLetterAscii

    print(decryption)


decrypt("dnotq")

# encrypt("crime")