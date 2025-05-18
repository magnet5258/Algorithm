km = int(input())
sides = []
for _ in range(6):
    direction, length = map(int, input().split())
    sides.append((direction, length))

max_width = 0
max_height = 0
max_width_idx = 0
max_height_idx = 0

for i in range(6):
    d, l = sides[i]
    if d in (1, 2):
        if l > max_width:
            max_width = l
            max_width_idx = i
    else:
        if l > max_height:
            max_height = l
            max_height_idx = i

small_width = sides[(max_height_idx + 3) % 6][1]
small_height = sides[(max_width_idx + 3) % 6][1]
area = (max_width * max_height) - (small_width * small_height)

print(area * km)