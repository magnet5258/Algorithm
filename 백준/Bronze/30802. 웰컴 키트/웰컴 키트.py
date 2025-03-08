N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())
cnt = 0
for size in sizes:
    if size % T == 0:
        cnt += size // T
    else:
        cnt += size // T + 1
print(f'{cnt}\n{N // P} {N % P}')