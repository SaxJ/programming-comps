letters = "abcdefghijklmnopqrstuvwxyz"

T = int(input())
for t in range(T):
    n, a, b = [int(x) for x in input().split(" ")]
    counts = {}

    # initialise string
    s = ""
    for i in range(b):
        l = letters[i % 26]
        s += l
        counts[l] = 1
    while len(s) < a:
        s += "a"
        counts["a"] += 1

    letter = b % 26
    current = 1
    while len(s) < n:
        removedChar = s[current - 1]
        counts[removedChar] -= 1
        if counts[removedChar] == 0:
            counts.pop(removedChar, None)

        distinct = len(counts.keys())
        if distinct < b:
            nextLetter = letters[letter]
            s += nextLetter
            if nextLetter not in counts:
                counts[nextLetter] = 1
            letter = (letter + 1) % 26
        else:
            s += removedChar
        current += 1
    print(s)
