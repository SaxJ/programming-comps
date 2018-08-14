T = int(input())

for c in range(T):
  N = int(input())

  i = N
  while True:
    div = True
    for d in range(1, N+1):
      if i % d != 0:
        div = False
    if div:
      print(i)
      break
    i += 1
