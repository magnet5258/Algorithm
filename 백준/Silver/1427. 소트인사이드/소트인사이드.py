from collections import Counter

N = input()
cnt = Counter(N)
answer = ''.join([key * value for key, value in sorted(cnt.items(), reverse=True)])

print(answer)