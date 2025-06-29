N = int(input())
weights = sorted(list(map(int, input().split())))

target = 1
for w in weights:
    if w > target:
        break
    target += w

print(target)