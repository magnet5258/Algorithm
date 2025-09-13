N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

left, right = 0, len(liquid) - 1
result = (left, right)
answer = float('inf')
while left < right:
    s = liquid[left] + liquid[right]
    if abs(s) < answer:
        answer = abs(s)
        result = (liquid[left], liquid[right])
    if s < 0:
        left += 1
    elif s > 0:
        right -= 1
    else:
        print(liquid[left], liquid[right])
        exit()

print(*result)