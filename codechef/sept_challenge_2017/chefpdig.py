T = int(input())
for t in range(T):
    N = input()
    seen = {}
    for c in N:
        if c in seen:
            seen[c] = 2
        else:
            seen[c] = 1

    nums = []
    for k in seen.keys():
        for i in range(seen[k]):
            nums.append(k)

    codes = {}
    for ix, i in enumerate(nums):
        for jx, j in enumerate(nums):
            if ix != jx:
                codes[int(i+j)] = True

    s = ''
    for c in codes.keys():
        if c >= 65 and c <= 90:
            s = s + chr(c)

    print(''.join(sorted(s)))
