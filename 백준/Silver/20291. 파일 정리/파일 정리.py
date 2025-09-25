from collections import defaultdict

N = int(input())
files = defaultdict(int)
for _ in range(N):
    a, b = input().split('.')
    files[b] += 1

sorted_files = sorted(files.items(), key=lambda x: x[0])
for a, b in sorted_files:
    print(a, b)