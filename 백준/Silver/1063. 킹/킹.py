row = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
column = list(range(1, 9))

king, rock, N = input().split()
N = int(N)
lst = [input() for _ in range(N)]
king_rc = [row.index(king[0]), int(king[1])]
rock_rc = [row.index(rock[0]), int(rock[1])]

moves = {
    'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1),
    'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)
}

for move in lst:
    if move in moves:
        dr, dc = moves[move]
        new_king = [king_rc[0] + dr, king_rc[1] + dc]
        if 1 <= new_king[0] <= 8 and 1 <= new_king[1] <= 8:
            if new_king == rock_rc:
                new_rock = [rock_rc[0] + dr, rock_rc[1] + dc]
                if 1 <= new_rock[0] <= 8 and 1 <= new_rock[1] <= 8:
                    rock_rc = new_rock
                else:
                    continue
            king_rc = new_king

print(row[king_rc[0]] + str(king_rc[1]))
print(row[rock_rc[0]] + str(rock_rc[1]))