G = int(input())
P = int(input())

parent = list(range(G + 1))

def find(x):
    if parent[x] != x:               
        parent[x] = find(parent[x])
    return parent[x]

cnt = 0
for _ in range(P):
    g = int(input())
    gate = find(g)
    if gate == 0:
        break
    cnt += 1
    parent[gate] = find(gate - 1)

print(cnt)