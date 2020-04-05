import sys

def bitFlip(c):
    return '1' if c == '0' else '0'

def flip(s):
    return ''.join([bitFlip(c) for c in s])

def reverse(s):
    return ''.join(list(reversed(s)))

def getOp(before, after):
    flipped = flip(before)
    rev = reverse(before)
    if before == after:
        return 'none'
    if after == rev:
        return 'reversed'
    if after == flipped:
        return 'flipped'
    return 'both'

def getCounts(ops):
    result = {}
    for o in ops:
        if o not in result:
            result[o] = 1
        else:
            result[o] += 1
    return result

def getMin(counts):
    mn = 0
    mk = None
    for k in counts.keys():
        if mk is None or counts[k] < mn:
            mn = counts[k]
            mk = k
    return mk

def getOps(states):
    last = None
    ops = []
    for state in states:
        if last is None:
            last = state
            continue
        else:
            ops.append(getOp(last, state))
            last = state
    return ops

def applyOp(state, op):
    if op == 'reversed':
        return reverse(state)
    if op == 'flipped':
        return flip(state)
    if op == 'none':
        return state
    if op == 'both':
        return reverse(flip(state))

def applySeq(state, ops):
    steps = []
    steps.append(state)
    for op in ops:
        state = applyOp(state, op)
        steps.append(state)
    return steps

def guess(first, last, ops, out):
    possibleStarts = [([op], applyOp(first, op)) for op in ['reversed', 'flipped', 'none', 'both']]
    for o, start in possibleStarts:
        seq = o + ops
        end = applySeq(start, seq)
        if end == last:
            print(start)

def possible(state):
    return [(op, applyOp(state, op)) for op in ['reversed', 'flipped', 'none', 'both']]

#s = input()
#print("flip: {}".format(applyOp(s, 'flipped')))
#print("reverse: {}".format(applyOp(s, 'reversed')))
#print("both: {}".format(applyOp(s, 'both')))
#exit(0)

T, B = [int(x) for x in input().split(' ')]
for t in range(T):
    state = ''
    for b in range(1, B+1):
        print(b)
        state += input()

    print(state)

    result = input()
    if result == 'Y':
        continue
    else:
        exit(0)
        
