seen = {}

def getMaxLess(n):
    ks = seen.keys()
    m = None
    for k in ks:
        if k < n:
            if m is None:
                m = k
            elif k > m:
                m = k
    return m

def calc(until, start = 0, bits = 1, nibs = 0, byts = 0):
    bitAges = {0: 1}
    nibAges = {}
    byteAges = {}
    for i in range(2, until, 2):
        toNib = i - 2
        if toNib in bitAges:
            nibAges[i] = bitAges[toNib]
            del bitAges[toNib]
        
        toByte = i - 8
        if toByte in nibAges:
            byteAges[i] = nibAges[toByte]
            del nibAges[toByte]

        toBit = i - 16
        if toBit in byteAges:
            bitAges[i] = 2 * byteAges[toBit]
            del byteAges[toBit]

    bits = sum(bitAges.values())
    nibs = sum(nibAges.values())
    byts = sum(byteAges.values())
    seen[until] = (bits, nibs, byts)
    return '{} {} {}'.format(bits, nibs, byts)


cases = int(input())
for c in range(cases):
    n = int(input())
    maxLess = None
    if maxLess is None:
        #print('no maxless')
        print(calc(n))
    else:
        #print('maxless = {}'.format(maxLess))
        b, nb, y = seen[maxLess]
        print(calc(n, maxLess, b, nb, y))
