def calc(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b


def dfs(idx, total):
    global max_result

    if idx >= len(expression):
        max_result = max(max_result, total)
        return

    op = expression[idx - 1] if idx != 0 else '+'
    num = int(expression[idx])

    dfs(idx + 2, calc(total, op, num))

    if idx + 2 < len(expression):
        next_num = int(expression[idx + 2])
        next_op = expression[idx + 1]
        bracket = calc(num, next_op, next_num)
        dfs(idx + 4, calc(total, op, bracket))


N = int(input())
expression = input()
max_result = float('-inf')
dfs(0, 0)
print(max_result)