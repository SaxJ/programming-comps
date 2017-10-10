T = int(input())

state = []
amounts = {}
def inc(l, r, amount):
    for i in range(l-1, r):
        state[i] += amount
        state[i] = state[i] % (10 ** 9 + 7)

def addAmount(cmd):
    if cmd in amounts:
        amounts[cmd] += 1
    else:
        amounts[cmd] = 1

for t in range(T):
    n, m = [int(x) for x in input().split(' ')]
    state = [0] * n
    commands = []
    execStack = []
    amounts = {}
    for i in range(m):
        c, l, r = [int(x) for x in input().split(' ')]
        commands.append([c,l,r, i])

        if c == 1:
            addAmount(i)
        else:
            execStack.append([c, l, r, i])

    while len(execStack) != 0:
        c, l, r, i = execStack.pop()
        if c == 1:
            addAmount(i)
        else:
            for x in range(l-1, r):
                execStack.append(commands[x])

    for k in amounts.keys():
        c, l, r, i = commands[k]
        inc(l, r, amounts[k])

    state = [str(r) for r in state]
    print(' '.join(state))
