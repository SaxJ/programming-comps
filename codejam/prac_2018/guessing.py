cases = int(input())

for c in range(cases):
    a, b = [int(x) for x in input().split(' ')]
    n = int(input())

    for i in range(n):
        guess = (a + b) // 2
        if (b - a) == 1:
            guess = b

        print(guess)
        response = input()
        if response == 'TOO_SMALL':
            a = guess + 1
        elif response == 'TOO_BIG':
            b = guess - 1
        else:
            break
