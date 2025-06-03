def change(num, total):
    global min_cnt

    if num > target:
        return

    if num == target:
        min_cnt = min(min_cnt, total)
        return

    change(num * 2, total + 1)
    change(num * 10 + 1, total + 1)


start, target = map(int, input().split())
min_cnt = float('inf')
change(start, 1)
print(min_cnt if min_cnt != float('inf') else -1)