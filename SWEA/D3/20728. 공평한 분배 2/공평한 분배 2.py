T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    candy = list(map(int, input().split()))
    candy.sort(reverse=True)
    min_diff = float('inf')
    for i in range(N - K + 1):
        min_diff = min(min_diff, (candy[i] - candy[i + K - 1]))
    print(f'#{test_case} {min_diff}')