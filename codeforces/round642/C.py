
squares = {
    1:0,
    3:8
}

maxN = 1
T = int(input())
for t in range(T):
    n = int(input())
    if n > maxN:
        for i in range(maxN + 2, n + 2, 2):
            outer = n + (2 * (n - 1)) + (n - 2);
            level = n / 2;
            layer = outer * level;
        maxN = n
