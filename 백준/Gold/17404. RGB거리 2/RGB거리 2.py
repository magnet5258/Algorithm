N = int(input())
color_price = []
for _ in range(N):
    R, B, G = map(int, input().split())
    color_price.append([R, B, G])

dp1 = [[0] * 3 for _ in range(N)]
dp1[0] = [color_price[0][0], float('inf'), float('inf')]
for i in range(1, N):
    dp1[i][0] = min(dp1[i - 1][1], dp1[i - 1][2]) + color_price[i][0]
    dp1[i][1] = min(dp1[i - 1][0], dp1[i - 1][2]) + color_price[i][1]
    dp1[i][2] = min(dp1[i - 1][0], dp1[i - 1][1]) + color_price[i][2]

dp2 = [[0] * 3 for _ in range(N)]
dp2[0] = [float('inf'), color_price[0][1], float('inf')]
for i in range(1, N):
    dp2[i][0] = min(dp2[i - 1][1], dp2[i - 1][2]) + color_price[i][0]
    dp2[i][1] = min(dp2[i - 1][0], dp2[i - 1][2]) + color_price[i][1]
    dp2[i][2] = min(dp2[i - 1][0], dp2[i - 1][1]) + color_price[i][2]

dp3= [[0] * 3 for _ in range(N)]
dp3[0] = [float('inf'), float('inf'), color_price[0][2]]
for i in range(1, N):
    dp3[i][0] = min(dp3[i - 1][1], dp3[i - 1][2]) + color_price[i][0]
    dp3[i][1] = min(dp3[i - 1][0], dp3[i - 1][2]) + color_price[i][1]
    dp3[i][2] = min(dp3[i - 1][0], dp3[i - 1][1]) + color_price[i][2]

result = min(dp1[N - 1][1], dp1[N - 1][2], dp2[N - 1][0], dp2[N - 1][2], dp3[N - 1][0], dp3[N - 1][1])
print(result)