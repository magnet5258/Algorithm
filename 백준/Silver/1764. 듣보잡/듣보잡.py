N, M = map(int, input().split())
listen = set(input() for _ in range(N))
watch = set(input() for _ in range(M))
both = sorted(listen & watch)

print(len(both))
for p in both:
    print(p)