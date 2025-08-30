N, K = map(int, input().split())
temp = list(map(int, input().split()))
sum_temp = []

for i in range(N - K + 1):
    sum_temp.append(sum(temp[i:i + K]))

print(max(sum_temp))