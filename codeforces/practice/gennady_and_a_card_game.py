r, s = [c for c in input()]
hand = input().split(' ')
for card in hand:
    if card[0] == r or card[1] == s:
        print('YES')
        exit(0)
print('NO')
