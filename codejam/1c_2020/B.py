def encrypt(n, digits):
    s = ''
    for d in n:
        s += digits[int(d)]
    return s

def test(pairs, d):
    for k in pairs:
        actual = encrypt(k, d)
        print("{} = {}".format(k, actual))
        if actual != pairs[k]:
            return False
    return True

T = int(input())
for t in range(T):
    u = int(input())
    maxes = {}
    pairs = {}
    ableZero = {}
    for i in range(10000):
        qi, resp = input().split(' ')
        query = int(qi)
        pairs[qi] = resp

        digits = len(resp)
        for c in resp:
            if c not in maxes:
                ableZero[c] = True
                maxes[c] = 9

        if query < 0:
            if len(resp) == u:
                ableZero[resp[0]] = False
            continue
        
        div = 10 ** (digits - 1)
        if len(str(query)) == digits:
            limit = query // div
            maxes[resp[0]] = min(maxes[resp[0]], limit)
            ableZero[resp[0]] = False

    cs = [(c, maxes[c]) for c in maxes]
    cs.sort(key=lambda x: x[1])

    nines = [p[0] for p in cs if p[1] == 9 and not ableZero[p[0]]]
    zeros = [p[0] for p in cs if p[1] == 9 and ableZero[p[0]]]
    notNines = [p[0] for p in cs if p[1] != 9]
    optionA = zeros[0] + ''.join(notNines) + nines[0]
    print("Case #{}: {}".format(t + 1, optionA))
