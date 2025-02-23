def reorderSpaces(text):
    """
    :type text: str
    :rtype: str
    """
    print("content is", text)
    total_spaces = 0
    last_char_is_alphabet = False
    word_count = 0
    last_char_pos = 0

    for index, i in enumerate(text):
       if i == " ":
           total_spaces += 1
           if last_char_is_alphabet:
               word_count += 1
           last_char_is_alphabet = False
       else:
           last_char_pos = index
           last_char_is_alphabet = True

    if last_char_is_alphabet:
        word_count += 1

    if word_count == 1 :
        word_count += 1

    space_at_words, space_at_word_end = divmod(total_spaces, (word_count-1))

    result = ""
    last_char_is_alphabet = False
    for index, j in enumerate(text):
        if j == " ":
            if last_char_is_alphabet and last_char_pos > index:
                result += " " * space_at_words
            last_char_is_alphabet = False
            continue
        else:
            result += j
            last_char_is_alphabet = True
    if space_at_word_end > 0:
        result += " " * space_at_word_end

    print(total_spaces, word_count)
    print("space_at_words", "///", "space_at_word_end", ":", space_at_words, space_at_word_end)
    print("Result is ........................................")
    print(result)



# text = "  this   is  a sentence "
# text = " practice   makes   perfect"
# text = "this   is   a   sentence"
text = "  hello"
reorderSpaces(text)