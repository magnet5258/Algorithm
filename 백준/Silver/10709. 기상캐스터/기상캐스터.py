H, W = map(int, input().split())
for _ in range(H):
    cloud = input()
    predict = []
    cur_idx = 0
    check = set()
    for i in range(len(cloud)):
        if cloud[i] == 'c':
            predict.append(0)
            check.add(cloud[i])
            cur_idx = i
        else:
            if 'c' in check:
                predict.append(i - cur_idx)
            else:
                predict.append(-1)
    print(*predict)
            