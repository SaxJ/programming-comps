T = int(input())

for t in range(T):
    n = int(input())
    parents = {}
    children = {}

    for i in range(n):
        frm = input()
        to = input()
        
        parents[to] = frm
        children[frm] = to

    head = None
    for k in children:
        if k not in parents:
            head = k

    order = []
    while True:
        v = children[head]
        order.append("{0}-{1}".format(head, v))

        if v in children:
            head = v
        else:
            break

    print(' '.join(order))
