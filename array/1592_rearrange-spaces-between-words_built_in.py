def reorderSpaces(text):
    """
    :type text: str
    :rtype: str
    """
    words = text.split()
    spaces_count = text.count()
    word_len = len(words)

    if words > 1:
        div, mod = divmod(spaces_count, words-1)
        return  (' ' * div).join(words) + ' ' * mod

    return words[0]  + ' ' * spaces_count



text = "  this   is  a sentence "
# text = " practice   makes   perfect"
# text = "this   is   a   sentence"
# text = "  hello"
reorderSpaces(text)