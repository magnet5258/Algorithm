N, S = map(int, input().split())
lst = list(map(int, input().split()))

length = float('inf')
left = right = 0
total = 0
while True:
    if total >= S:
        length = min(length, right - left)
        total -= lst[left]
        left += 1
    elif right == N:
        break
    else:
        total += lst[right]
        right += 1

if length == float('inf'):
    print(0)
else:
    print(length)