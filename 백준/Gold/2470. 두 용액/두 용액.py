N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

answer = []
total = float('inf')
left, right = 0, N - 1
while left < right:
    if abs(liquid[left] + liquid[right]) < total:
        answer = [liquid[left], liquid[right]]
        total = abs(liquid[left] + liquid[right])

    if liquid[left] + liquid[right] > 0:
        right -= 1
    elif liquid[left] + liquid[right] < 0:
        left += 1
    else:
        break

print(*answer)