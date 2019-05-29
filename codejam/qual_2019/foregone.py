T = int(input())
pairs = {
    '0': ('0', '0'),
    '1': ('1', '0'),
    '2': ('1', '1'),
    '3': ('1', '2'),
    '4': ('2', '2'),
    '5': ('2', '3'),
    '6': ('3', '3'),
    '7': ('5', '2'),
    '8': ('5', '3'),
    '9': ('6', '3')
}

for t in range(T):
    n = input()
    a = []
    b = []
    for d in n:
        (x, y) = pairs[d]
        a.append(x)
        b.append(y)

    na = ''.join(a).lstrip('0')
    nb = ''.join(b).lstrip('0')

    print('Case #{}: {} {}'.format(t + 1, na, nb))
