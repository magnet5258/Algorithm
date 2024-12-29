a = int(input())
b = list(map(int, input().split()))
sorted_b = sorted(b)
print(sorted_b[len(b) // 2])