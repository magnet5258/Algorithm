N = int(input())
min_dp = list(map(int, input().split()))
max_dp = min_dp[:]

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    prev_min_dp = min_dp[:]
    prev_max_dp = max_dp[:]

    min_dp[0] = min(prev_min_dp[0], prev_min_dp[1]) + a
    min_dp[1] = min(prev_min_dp[0], prev_min_dp[1], prev_min_dp[2]) + b
    min_dp[2] = min(prev_min_dp[1], prev_min_dp[2]) + c

    max_dp[0] = max(prev_max_dp[0], prev_max_dp[1]) + a
    max_dp[1] = max(prev_max_dp[0], prev_max_dp[1], prev_max_dp[2]) + b
    max_dp[2] = max(prev_max_dp[1], prev_max_dp[2]) + c

print(max(max_dp), min(min_dp))