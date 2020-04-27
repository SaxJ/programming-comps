def indexOf(needle, haystack, startFrom):
    for i in range(startFrom, len(haystack)):
        good = True
        output = ""
        for j, c in enumerate(needle):
            h = haystack[i + j]
            if not (c == h or h == "*"):
                good = False
                break
            output += c

        if good:
            print("{} in {} at {}".format(needle, haystack, i))
            return (i, output)
    return (-1, "")


def combine(aStr, bStr):
    success = True
    parts = aStr.split("*")
    startFrom = 0
    result = ""
    for part in parts:
        if part == "":
            result += "*"
            continue
        (idx, output) = indexOf(part, bStr, startFrom)
        if idx == -1:
            success = False
            break
        else:
            result += output
            startFrom = idx + len(part)
    return (success, result)


T = int(input())
for t in range(T):
    N = int(input())
    last = "*"
    fail = False
    for n in range(N):
        current = input()
        (lastInCurrent, output) = combine(last, current)
        if lastInCurrent:
            print(last)
            last = current
            continue
        currentInLast, output = combine(current, last)
        if currentInLast:
            last = current
            continue

        fail = True
    result = "*" if fail else last.replace("*", "A")
    print("Case #{}: {}".format(t + 1, result))
