N = int(input())
max_score = 0
for _ in range(N):
    lst = list(map(int, input().split()))
    score = 0
    score += max(lst[:2]) + sum(sorted(lst[2:])[3:])
    max_score = max(max_score, score)

print(max_score)