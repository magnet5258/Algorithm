from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

LIS = []
for x in A:
    i = bisect_left(LIS, x)
    if i == len(LIS):
        LIS.append(x)
    else:
        LIS[i] = x

print(len(LIS))