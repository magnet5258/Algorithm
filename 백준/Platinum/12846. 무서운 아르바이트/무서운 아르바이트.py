n = int(input())
pays = list(map(int, input().split()))
stack = []
max_pay = 0
i = 0

while i < n:
    if not stack or pays[stack[-1]] <= pays[i]:
        stack.append(i)
        i += 1
    else:
        pay = stack.pop()
        days = i if not stack else i - stack[-1] - 1
        max_pay = max(max_pay, pays[pay] * days)

while stack:
    pay = stack.pop()
    days = i if not stack else i - stack[-1] - 1
    max_pay = max(max_pay, pays[pay] * days)

print(max_pay)