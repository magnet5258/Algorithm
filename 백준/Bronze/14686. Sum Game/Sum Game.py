N = int(input())
Swifts = list(map(int, input().split()))
Semaphores = list(map(int, input().split()))

K = 0
total_1 = 0
total_2 = 0

i = 1
while i < N + 1:
    total_1 += Swifts[i - 1]
    total_2 += Semaphores[i - 1]
    if total_1 == total_2:
        K = i
    i += 1

print(K)