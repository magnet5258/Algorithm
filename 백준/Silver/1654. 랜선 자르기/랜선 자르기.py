K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]
start = 1
end = max(lines)
ans = 0

while start <= end:
    mid = (start + end) // 2
    cnt = sum(line // mid for line in lines)
    if cnt >= N:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)