def is_possible(n):
    for ch in str(n):
        if int(ch) in broken:
            return False
    return True


N = int(input())
M = int(input())

if M == 0:
    broken = []
else:
    broken = list(map(int, input().split()))
min_clicks = abs(N - 100)

for num in range(1000001):
    if is_possible(num):
        press = len(str(num))
        move = abs(N - num)
        min_clicks = min(min_clicks, press + move)

print(min_clicks)