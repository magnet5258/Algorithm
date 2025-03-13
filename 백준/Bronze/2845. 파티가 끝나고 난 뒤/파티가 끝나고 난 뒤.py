L, P = map(int, input().split())
nums = list(map(int, input().split()))
ans = []
for num in nums:
    ans.append(num - L * P)
print(*ans)