import sys

N, M = map(int, sys.stdin.readline().split())

password = {}
for _ in range(N):
    site, pwd = sys.stdin.readline().split()
    password[site] = pwd

for _ in range(M):
    site = sys.stdin.readline().strip()
    print(password[site])
