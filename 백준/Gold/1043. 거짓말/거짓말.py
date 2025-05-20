N, M = map(int, input().split())
num, *ppl = map(int, input().split())
ppl = set(ppl)
ans = 0

party_lst = []
for _ in range(M):
    n, *p = map(int, input().split())
    party_lst.append(p)

changed = True
while changed:
    changed = False
    for party in party_lst:
        if set(party) & ppl:
            new_ppl = set(party) | ppl
            if new_ppl != ppl:
                ppl = new_ppl
                changed = True

if num == 0:
    ans = M
else:
    for party in party_lst:
        if not (set(party) & ppl):
            ans += 1

print(ans)