s = input()
count = 0
for i in range(len(s) - 4):
    for j in range(i + 3, len(s)):
        sub = s[i:j+1]
        n = int(sub)
        if n % 2019 == 0:
            count += 1
print(count)
