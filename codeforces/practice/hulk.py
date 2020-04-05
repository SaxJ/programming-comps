n = int(input())
parts = []
for i in range(1, n+1):
    s = ''
    if i % 2 == 0:
        s += 'I love '
    else:
        s += 'I hate '
    if i == n:
        s += 'it'
    else:
        s += 'that'
    parts.append(s)
print(' '.join(parts))
    
