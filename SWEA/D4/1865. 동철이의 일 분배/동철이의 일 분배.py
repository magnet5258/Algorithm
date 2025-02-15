def max_percentage(idx, per):
    global max_per

    if per <= max_per:
        return
    if idx == N:
        max_per = max(max_per, per)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            max_percentage(idx + 1, per * arr[idx][i] * 0.01)
            visited[i] = False


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_per = 0
    visited = [False] * N
    max_percentage(0, 1)
    ans = max_per * 100
    print(f'#{test_case} {ans:.6f}')