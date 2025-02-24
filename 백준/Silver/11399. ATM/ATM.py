N = int(input())
P = list(map(int, input().split()))
P.sort()
time = 0
sum_time = 0
for i in P:
    time += i
    sum_time += time
print(sum_time)