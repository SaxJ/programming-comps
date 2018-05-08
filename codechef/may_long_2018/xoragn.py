import itertools

T = int(input())
for t in range(T):
    N = int(input())
    seq = [int(x) for x in input().split(' ')]
    hd, lstB = seq[0], seq[1:]
    for n in lstB:
        hd = hd ^ n

    print(hd)
