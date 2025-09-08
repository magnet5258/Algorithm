N, M = map(int, input().split())
trees = list(map(int, input().split()))

low, high = 0, max(trees)
answer = 0

while low <= high:
    mid = (low + high) // 2
    cut = 0
    for tree in trees:
        if tree - mid > 0:
            cut += tree - mid
    if cut >= M:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)