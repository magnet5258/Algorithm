from collections import defaultdict

N = int(input())
words = [input() for _ in range(N)]
weight = defaultdict(int)

for word in words:
    length = len(word)
    for i, ch in enumerate(word):
        pos_value = 10 ** (length - i - 1)
        weight[ch] += pos_value

sorted_items = sorted(weight.items(), key=lambda x: x[1], reverse=True)

num_dict = {}
num = 9
for key, value in sorted_items:
    num_dict[key] = num
    num -= 1

answer = 0
for word in words:
    num_lst = []
    for alphabet in word:
        num_lst.append(str(num_dict[alphabet]))
    answer += int(''.join(num_lst))

print(answer)