def factors(n):    
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True    

n = 12345312
print(factors(n))
print([z for z in factors(n) if is_prime(z)])
x = len(factors(n))
k = len([z for z in factors(n) if is_prime(z)])
print(f"x = {x}")
print(f"k = {k}");

T = int(input())
for t in range(T):
    x, k = [int(x) for x in input().split(' ')]
    fs = [a - 1 for a in factors(x) if is_prime(a)]
    print(f"fs = {fs}")
    if len(fs) == k:
        print(1)
    else:
        print(0)
    
