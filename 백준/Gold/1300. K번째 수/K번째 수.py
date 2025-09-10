N = int(input())
k = int(input())

left, right = 1, N ** 2
answer = 0
while left <= right:
    mid = (left + right) // 2
    total = sum(min(N, mid // i) for i in range(1, N + 1))
    if total >= k:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)