# words = ["This", "is", "an", "example", "of", "text", "justification."]
# words = ["What", "must", "be", "acknowledgment", "shall", "be"]
# words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16


def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    result = []
    line = []
    line_count = 0
    for w in words:
        word_len = len(w)


        if word_len + line_count + len(line) <= maxWidth:
            line.append(w)
            line_count += word_len
            continue

        spaces = maxWidth - line_count
        if len(line) == 1:
            result.append(line[0] + ' ' * spaces)
        else:
            spaces_bw_words, extra_spaces = divmod(spaces, max(1, len(line)-1))

            i = 0
            while extra_spaces > 0:
                line[i] += ' '
                extra_spaces -= 1
                i += 1
            result.append(
                (' ' * spaces_bw_words).join(line)
            )

        line_count = word_len
        line = [w]
    result.append(
        ' '.join(line)
    )
    return result








if __name__ == "__main__":
    print(fullJustify(words, maxWidth))
