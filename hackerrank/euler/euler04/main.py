def find(col, n):
  l = 0
  u = len(col) - 1
  while l < u:
    i = (l + u) // 2
    if n > col[i]:
      l = i + 1
    elif n < col[i]:
      u = i - 1
    else:
      return col[i-1]
  if u < l:
    return col[u]
  else:
    return col[l]

def get(col, n):
  lst = 0
  for p in col:
    if p >= n:
      return lst
    lst = p

T = int(input())
palas = []
for i in range(100, 1000):
  for j in range(i, 1000):
    p = i * j
    s = str(p)
    if s[::-1] == s:
      palas.append(p)
palas.sort()

for c in range(T):
  N = int(input())
  p = get(palas, N)
  print(p)
