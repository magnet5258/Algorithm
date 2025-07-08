T = int(input())
for _ in range(T):
    N = int(input())
    grades = []
    cnt = 0
    for _ in range(N):
        x, y = map(int, input().split())
        grades.append((x, y))
    grades.sort()
    check_score = float('inf')
    for x, y in grades:
        if y < check_score:
            cnt += 1
            check_score = min(y, check_score)
    print(cnt)