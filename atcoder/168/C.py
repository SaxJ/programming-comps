import math

a, b, h, m = [int(x) for x in input().split(' ')]

a1 = (2 * math.pi) * (h / 12) + (2 * math.pi) * (m / (60 * 12))
a2 = (2 * math.pi) * (m / 60)
diff = max(a1, a2) - min(a1, a2)
if diff > math.pi:
    diff = (2 * math.pi) - diff

ds = a * a + b * b - 2 * a * b * math.cos(diff)
print(math.sqrt(ds))
