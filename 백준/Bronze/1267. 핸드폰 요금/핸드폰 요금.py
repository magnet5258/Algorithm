N = int(input())
time = list(map(int, input().split()))

Y, M = 0, 0
for t in time:
    Y += (t // 30 * 10) + 10
    M += (t // 60 * 15) + 15

if Y > M:
    print('M', M)
elif Y < M:
    print('Y', Y)
else:
    print('Y', 'M', Y)