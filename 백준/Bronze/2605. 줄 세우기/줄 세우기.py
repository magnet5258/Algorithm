N = int(input())
lst = list(map(int, input().split()))
ans = []
for i in range(N):
    ans.insert(lst[i], i + 1)
ans.reverse()
print(' '.join(map(str, ans)))