N, X = map(int, input().split())
visitors = list(map(int, input().split()))

total_visitors = []
total = sum(visitors[:X])
total_visitors.append(total)
i = 0
while i < N - X:
    total = total - visitors[i] + visitors[i + X]
    i += 1
    if total > total_visitors[-1]:
        total_visitors = [total]
    elif total == total_visitors[-1]:
        total_visitors.append(total)
    else:
        continue

if total_visitors[-1] == 0:
    print('SAD')
else:
    print(total_visitors[-1])
    print(len(total_visitors))