def find_subsequence(start, cur_subs, cur_sum):
    if cur_sum == K:
        result.append(cur_subs[:])
        return
 
    if cur_sum > K:
        return
 
    for i in range(start, N):
        cur_subs.append(lst[i])
        find_subsequence(i + 1, cur_subs, cur_sum + lst[i])
        cur_subs.pop()
 
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    result = []
    find_subsequence(0, [], 0)
    print(f'#{test_case} {len(result)}')