from collections import Counter

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
check = Counter(cards)
print(*[check[num] for num in nums])