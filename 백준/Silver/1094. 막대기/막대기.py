X = int(input())
branches = [64, 32, 16, 8, 4, 2, 1]
cnt = 0
for branch in branches:
    if X == 0:
        break
    elif branch <= X:
        cnt += 1
        X -= branch

print(cnt)