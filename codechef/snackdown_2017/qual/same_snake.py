cases = int(input())

def between(x, a, b):
    if a > b:
        return (b <= x <= a)
    else:
        return (a <= x <= b)

for c in range(cases):
    x11, y11, x12, y12 = [int(x) for x in input().split(' ')]
    x21, y21, x22, y22 = [int(x) for x in input().split(' ')]

    if x11 == x12: # vertical
        if x21 == x22:
            if between(y21, y11, y12) or between(y22, y11, y12):
                print('yes')
            else:
                print('no')
        else:
            if (y21 == y11) or (y21 == y12) or (y22 == y11) or (y22 == y12):
                print('yes')
            else:
                print('no')
    else: #horizontal
        if y21 == y22:
            if between(x21, x11, x12) or between(x22, x11, x12):
                print('yes')
            else:
                print('no')
        else:
            if (x21 == x11) or (x21 == x12) or (x22 == x11) or (x22 == x12):
                print('yes')
            else:
                print('no')
