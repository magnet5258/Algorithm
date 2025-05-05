from collections import deque

S = input()
status = deque([0, 1])
for i in range(len(S) - 1):
    if S[i] > S[i + 1] and status[-1] == 1:
        S = S[:i + 1][::-1] + S[i + 1:]
        status.rotate(1)
    if S[i] < S[i + 1] and status[-1] == 0:
        S = S[:i + 1][::-1] + S[i + 1:]
        status.rotate(1)

print(min(S, S[::-1]))