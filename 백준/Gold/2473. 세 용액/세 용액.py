N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

answer = float('inf')
result = (0, 0, 0)

for i in range(N - 2):
    left, right = i + 1, N - 1
    while left < right:
        s = liquid[i] + liquid[left] + liquid[right]
        if abs(s) < answer:
            answer = abs(s)
            result = (liquid[i], liquid[left], liquid[right])
        if s < 0:
            left += 1
        elif s > 0:
            right -= 1
        else:
            print(liquid[i], liquid[left], liquid[right])
            exit()

print(*result)