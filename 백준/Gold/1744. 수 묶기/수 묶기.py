N = int(input())
positive = []
negative = []
ones = 0
zeros = 0
result = 0

for _ in range(N):
    num = int(input())
    if num > 1:
        positive.append(num)
    elif num == 1:
        ones += 1
    elif num == 0:
        zeros += 1
    else:
        negative.append(num)

positive.sort(reverse=True)
for i in range(0, len(positive) - 1, 2):
    result += positive[i] * positive[i+1]
if len(positive) % 2 == 1:
    result += positive[-1]

negative.sort()
for i in range(0, len(negative) - 1, 2):
    result += negative[i] * negative[i+1]
if len(negative) % 2 == 1:
    if zeros > 0:
        pass
    else:
        result += negative[-1]

result += ones

print(result)
