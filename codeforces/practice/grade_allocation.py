T = int(input())
for t in range(T):
    students, maxScore = [int(x) for x in input().split(' ')]
    scores = [int(x) for x in input().split(' ')]
    me = scores[0]
    total = sum(scores[1:])
    print(min(total + me, maxScore))

