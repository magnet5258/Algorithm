N = int(input())
ramen = list(map(int, input().split()))
money = 0

for i in range(N - 2):
    if ramen[i + 1] > ramen[i + 2]:
        min_2r = min(ramen[i], ramen[i + 1] - ramen[i + 2])
        money += min_2r * 5
        ramen[i] -= min_2r
        ramen[i + 1] -= min_2r

    min_3r = min(ramen[i], ramen[i + 1], ramen[i + 2])
    money += min_3r * 7
    ramen[i] -= min_3r
    ramen[i + 1] -= min_3r
    ramen[i + 2] -= min_3r

for i in range(N - 1):
    min_2r = min(ramen[i], ramen[i + 1])
    money += min_2r * 5
    ramen[i] -= min_2r
    ramen[i + 1] -= min_2r

money += sum(ramen) * 3

print(money)