K = int(input())
N = int(input())

answer = 0
time = 210
for _ in range(N):
    T, Z = input().split()
    time -= int(T)
    if time <= 0:
        answer = K
        break
    if Z == 'T':
        K += 1
        if K > 8:
            K = 1

print(answer)