chess = [1, 1, 2, 2, 2, 8]
piece = list(map(int, input().split()))
diff = []
for a, b in zip(chess, piece):
    diff.append(a - b)
print(*diff)