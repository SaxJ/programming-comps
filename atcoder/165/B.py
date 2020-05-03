import math
x = int(input())

t = (math.log(x) - math.log(100)) / math.log(1 + 0.01)
print(math.ceil(t))
