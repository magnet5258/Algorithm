N = int(input())
room = []
for _ in range(N):
    start, end = map(int, input().split())
    room.append((start, end))
sorted_room = sorted(room, key=lambda x: (x[1], x[0]))
ans = 0
time = 0
for i in range(len(sorted_room)):
    if sorted_room[i][0] >= time:
        ans += 1
        time = sorted_room[i][1]
print(ans)