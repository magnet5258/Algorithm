n = int(input())
A = []
B = []
C = []
D = []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = [a + b for a in A for b in B]
CD = [c + d for c in C for d in D]
AB.sort()
CD.sort(reverse=True)

i, j = 0, 0
answer = 0
while i < len(AB) and j < len(CD):
    if AB[i] + CD[j] == 0:
        ab_val = AB[i]
        cd_val = CD[j]
        cnt_ab = 0
        while i < len(AB) and ab_val == AB[i]:
            cnt_ab += 1
            i += 1
        cnt_cd = 0
        while j < len(CD) and cd_val == CD[j]:
            cnt_cd += 1
            j += 1
        answer += cnt_ab * cnt_cd
    elif AB[i] + CD[j] < 0:
        i += 1
    else:
        j += 1

print(answer)