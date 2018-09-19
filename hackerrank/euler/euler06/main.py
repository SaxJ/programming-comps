T = int(input())

for c in range(T):
  N = int(input())
  sum = N * (N + 1) // 2
  sqs = N * (N + 1) * (2 * N + 1) // 6
  d = sum * sum - sqs

  print(abs(d))
