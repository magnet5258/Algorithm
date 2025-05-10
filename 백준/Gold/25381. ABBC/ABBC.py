from collections import deque

S = input()
A_pos, b_noA, b_withA = [], deque(), deque()
seen_A, cnt = False, 0

for i, ch in enumerate(S):
    if ch == 'A':
        seen_A = True
        A_pos.append(i)
    elif ch == 'B':
        (b_withA if seen_A else b_noA).append(i)
    elif ch == 'C':
        target = b_noA if b_noA else b_withA
        if target:
            target.popleft()
            cnt += 1

ai = bi = 0
while ai < len(A_pos) and bi < len(b_withA):
    if A_pos[ai] < b_withA[bi]:
        cnt += 1
        ai += 1
    bi += 1

print(cnt)