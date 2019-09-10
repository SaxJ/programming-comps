pisano = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]
levels = {}
count = 1
arr = pisano.copy()
while len(arr) > 1:
    arr = [x for (i,x) in enumerate(arr) if (i + 1) % 2 == 0]
    levels[count] = arr.copy()
    count += 1

def process(a):
    count = 1
    while len(a) > 1:
        a = [x for (i,x) in enumerate(a) if (i + 1) % 2 == 0]
        count += 1
    return (a, count - 1)

T = int(input())
for t in range(T):
    N = int(input())
    repeats = N // 60
    leftover = N % 60

    (val, depth) = process(pisano[:leftover])
    repeatAtDepth = levels[depth]
    arr = (repeatAtDepth * repeats) + val
    ans, _ = process(arr)
    print(ans[0])
