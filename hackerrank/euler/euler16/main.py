from math import pow
T = int(input())
for i in range(T):
    N = int(input())
    p = 2 ** N
    number = str(p)
    sum = 0
    for char in number:
        sum += int(char)
    print(sum)
