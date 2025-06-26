N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_result = float('-inf')
min_result = float('inf')

def cal(idx, cur_result, add, sub, mul, div):
    global max_result, min_result

    if idx == N:
        max_result = max(max_result, cur_result)
        min_result = min(min_result, cur_result)

    if add > 0:
        cal(idx + 1, cur_result + A[idx], add - 1, sub, mul, div)
    if sub > 0:
        cal(idx + 1, cur_result - A[idx], add, sub - 1, mul, div)
    if mul > 0:
        cal(idx + 1, cur_result * A[idx], add, sub, mul - 1, div)
    if div > 0:
        if cur_result >= 0:
            cal(idx + 1, cur_result // A[idx], add, sub, mul, div - 1)
        else:
            cal(idx + 1, -(-cur_result // A[idx]), add, sub, mul, div - 1)

cal(1, A[0], add, sub, mul, div)

print(max_result)
print(min_result)