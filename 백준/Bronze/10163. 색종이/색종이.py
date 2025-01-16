N = int(input())
arr = [[0] * 1001 for _ in range(1001)]
papers = []

for n in range(1, N + 1):
    si, sj, w, h = map(int, input().split())
    papers.append((si, sj, w, h))
    for i in range(si, si + h):
        for j in range(sj, sj + w):
            arr[i][j] = n

cnts = [0] * (N + 1)
for i in range(1001):
    for j in range(1001):
        if arr[i][j] != 0:
            cnts[arr[i][j]] += 1

print(*cnts[1:], sep = '\n')