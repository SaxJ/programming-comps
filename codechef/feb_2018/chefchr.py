T = int(input())

for t in range(T):
    line = input()
    count = 0

    i = 0
    while (i + 3) != len(line):
        check = {}
        check[line[i]] = True
        check[line[i+1]] = True
        check[line[i+2]] = True
        check[line[i+3]] = True

        if ('c' in check) and ('h' in check) and ('e' in check) and ('f' in check):
            count += 1
        i += 1

    if count == 0:
        print('normal')
    else:
        print('lovely {}'.format(count))
