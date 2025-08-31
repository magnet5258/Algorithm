from collections import defaultdict

N = int(input())
S = list(map(int, input().split()))

fruit_cnt = defaultdict(int)
left = 0
max_len = 0

for right in range(N):
    fruit_cnt[S[right]] += 1
    while len(fruit_cnt) > 2:
        fruit_cnt[S[left]] -= 1
        if fruit_cnt[S[left]] == 0:
            del fruit_cnt[S[left]]
        left += 1

    max_len = max(max_len, right - left + 1)

print(max_len)