N = int(input())
K = int(input())
sensors = list(map(int, input().split()))
sensors.sort()

diff = []
for i in range(N - 1):
    diff.append(sensors[i + 1] - sensors[i])

diff.sort(reverse=True)
print(sum(diff[K - 1:]))