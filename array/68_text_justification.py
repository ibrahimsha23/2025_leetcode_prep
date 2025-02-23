words = ["This", "is", "an", "example", "of", "text", "justification."]
# words = ["What", "must", "be", "acknowledgment", "shall", "be"]
# words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 16


def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    result = []
    cursor = ""
    cursor_limit = 16
    i = 0
    words_len = len(words)
    empty_pad = " "
    while i < words_len:
        word = words[i]
        word_len = len(word)

        if cursor_limit >= word_len :
            cursor += word
            cursor_limit -= word_len

            if cursor_limit >= 1:
                cursor += empty_pad
                cursor_limit -= 1

            i += 1
        else:
            print("cursor limit", cursor_limit)
            result.append(cursor)
            cursor = ""
            cursor_limit = 16
    if cursor_limit < maxWidth:
        for i in range(cursor_limit):
            cursor += " "
        result.append(cursor)



    print(result)




    return result

if __name__ == "__main__":
    print(fullJustify(words, maxWidth))
