N = int(input())
stairs = [int(input()) for _ in range(N)]

if N == 1:
    ans = stairs[0]
elif N == 2:
    ans = stairs[0] + stairs[1]
elif N > 2:
    score = [0] * N
    score[0] = stairs[0]
    score[1] = stairs[0] + stairs[1]
    score[2] = stairs[2] + max(stairs[1], stairs[0])
    
    for i in range(3, N):
        score[i] = stairs[i] + max(stairs[i - 1] + score[i - 3], score[i - 2])

    ans = score[N - 1]

print(ans)