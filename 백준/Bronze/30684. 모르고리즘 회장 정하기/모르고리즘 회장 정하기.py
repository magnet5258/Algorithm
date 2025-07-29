N = int(input())
names = list(input() for _ in range(N))

answer = 'ZZZ'
for name in names:
    if len(name) == 3:
        answer = min(answer, name)

print(answer)