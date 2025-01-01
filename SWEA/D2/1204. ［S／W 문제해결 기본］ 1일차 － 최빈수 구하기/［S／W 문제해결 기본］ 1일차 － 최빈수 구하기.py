T = int(input())
for t in range(1, T + 1):
    _ = int(input())
    grade = list(map(int, input().split()))
    dic = {}
    for i in grade:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 0
    ans = max(dic, key = lambda k: (dic[k], k))
    print(f'#{t} {ans}')
    