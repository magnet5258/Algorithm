N = int(input())
person = []
rank = [1] * N
for i in range(N):
    x, y = map(int, input().split())
    person.append((x, y))
    for j in range(i):
        if person[j][0] < x and person[j][1] < y:
            rank[j] += 1
        elif person[j][0] > x and person[j][1] > y:
            rank[i] += 1

print(*rank)