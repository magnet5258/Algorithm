N, C = map(int, input().split())
home = []
for _ in range(N):
    num = int(input())
    home.append(num)
home.sort()

def can_install(dist):
    cnt = 1
    last = home[0]
    for i in range(1, N):
        if home[i] - last >= dist:
            cnt += 1
            last = home[i]
    return cnt >= C

left, right = 1, home[-1] - home[0]
answer = 0
while left <= right:
    mid = (left + right) // 2
    if can_install(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)