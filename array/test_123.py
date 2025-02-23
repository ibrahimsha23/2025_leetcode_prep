words =  ["This", "is", "an", "example", "of", "text", "justification."]


maxWidth = 16

result = ""
output = []
line = []
line_count = 0
for index, word in enumerate(words):
    word_len = len(word)
    if word_len + line_count + len(line) - 1 > maxWidth:
        spaces = maxWidth - line_count - len(line) - 1
        num, rem = divmod(spaces, max(1, len(line) - 1))
        result = ''
        for idx, line_ele in enumerate(line):
            result += line_ele
            result += ' ' * num

            if rem:
                result += ' ' * rem
                rem = 0
        output.append(result)
        line = []
        line_count = 0

    line.append(word)
    line_count += word_len


