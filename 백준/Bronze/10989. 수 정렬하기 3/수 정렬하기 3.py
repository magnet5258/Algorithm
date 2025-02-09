import sys

cnt = [0] * (10000 + 1)
N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    cnt[num] += 1

for i in range(len(cnt)):
    if cnt[i] != 0:
        for _ in range(cnt[i]):
            print(i)
