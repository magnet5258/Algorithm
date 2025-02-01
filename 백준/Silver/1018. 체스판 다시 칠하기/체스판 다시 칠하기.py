B = 'BWBWBWBW'
W = 'WBWBWBWB'
chess_B = []
chess_W = []

for i in range(8):
    if i % 2 == 0:
        chess_B.append(list(B))
        chess_W.append(list(W))
    else:
        chess_B.append(list(W))
        chess_W.append(list(B))

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

min_changes = float('inf')

for i in range(N - 7):
    for j in range(M - 7):
        count_B = 0
        count_W = 0
        for x in range(8):
            for y in range(8):
                if arr[i + x][j + y] != chess_B[x][y]:
                    count_B += 1
                if arr[i + x][j + y] != chess_W[x][y]:
                    count_W += 1
        min_changes = min(min_changes, count_B, count_W)
        
print(min_changes)
        