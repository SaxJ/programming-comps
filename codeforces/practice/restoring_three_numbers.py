nums = [int(x) for x in input().split(' ')]
[ab,ac,bc,abc] = sorted(nums)
a = abc - bc
b = abc - ac
c = abc - ab
print("{} {} {}".format(a, b, c))
