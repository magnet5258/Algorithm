N = int(input())
nums = set(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

result = []
for num in check:
    if num in nums:
        result.append(1)
    else:
        result.append(0)

print(*result)