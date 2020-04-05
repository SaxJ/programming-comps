def process(s):
    if len(s) == 0:
        return s

    i = 0
    op = False
    while i < len(s)-1:
        if s[i] == s[i+1]:
            left = s[:i]
            try:
                right = s[(i+2):]
            except IndexError:
                right = ''
            s = process(left) + process(right)
            op = True
        i += 1
    if op:
        return process(s)
    else:
        return s



stringIn = input()
stringOut = process(stringIn)
print('Empty String' if len(stringOut) == 0 else stringOut)
