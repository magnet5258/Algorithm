N = int(input())
M = int(input())
S = input()

i = 0
cnt = 0

while i < M - 1:
    if S[i] == 'I':
        temp = 0
        while i + 2 < M and S[i + 1] == 'O' and S[i + 2] == 'I':
            temp += 1
            i += 2
        if temp >= N:
            cnt += temp - N + 1
        else:
            i += 1
    else:
        i += 1

print(cnt)