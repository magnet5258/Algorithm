for t in range(1, 11):
    a = int(input())
    b = list(map(int, input().split()))
    answer = 0
    for i in range(2, a - 2):
        c = max(b[i - 2], b[i - 1], b[i + 1], b[i + 2])
        if b[i] > c:
            answer += b[i] - c
    print(f'#{t} {answer}')
