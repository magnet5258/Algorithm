N = int(input())
ingredients = []
for _ in range(N):
    s, b = map(int, input().split())
    ingredients.append((s, b))
min_diff = float('inf')

for bitmask in range(1, 1 << N):
    total_s = 1
    total_b = 0
    for i in range(N):
        if bitmask & (1 << i):
            total_s *= ingredients[i][0]
            total_b += ingredients[i][1]
    min_diff = min(min_diff, abs(total_s - total_b))

print(min_diff)