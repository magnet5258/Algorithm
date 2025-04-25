import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
if n == 0:
    print(0)
    sys.exit()
scores = sorted(data[1:])
criterion = int(n * 0.15 + 0.5)
filtered_scores = scores[criterion:n - criterion]
if not filtered_scores:
    print(0)
else:
    difficulty = int(sum(filtered_scores) / len(filtered_scores) + 0.5)
    print(difficulty)
