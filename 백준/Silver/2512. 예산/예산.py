N = int(input())
budget = list(map(int, input().split()))
M = int(input())

if sum(budget) <= M:
    print(max(budget))
    exit()
else:
    left, right = 0, M
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        total = 0
        for num in budget:
            if mid >= num:
                total += num
            else:
                total += mid
        if total <= M:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    print(answer)