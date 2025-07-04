N = int(input())
M = int(input())
S = input()

P = ''
for _ in range(N + 1):
    if P and P[-1] == 'I':
        P += 'O'
    P += 'I'

lp = len(P)
cnt = 0
for i in range(len(S)):
    if S[i:i + lp] == P:
        cnt += 1

print(cnt)