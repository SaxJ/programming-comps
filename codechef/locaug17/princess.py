def isPal(word):
    if len(word) < 2:
        return False

    for i in range(0, len(word) // 2):
        if word[i] != word[len(word) - 1 - i]:
            return False

    return True

T = int(input())
for t in range(T):
    seen = []
    line = input()

    found = False
    for c in line:
        seen.append(c)
        for i in range(len(seen), -1, -1):
            sub = seen[i:len(seen)]
            if isPal(sub):
                found = True
                break

        if found:
            break

    if found:
        print("YES")
    else:
        print("NO")
