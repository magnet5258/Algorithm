def check(a, b, op):
    if op == '<':
        return a < b
    else:
        return a > b

def find_num(idx, num_str):
    if idx == k + 1:
        result.append(num_str)
        return
    for i in range(10):
        if not visited[i]:
            if idx == 0 or check(int(num_str[-1]), i, ineqs[idx - 1]):
                visited[i] = True
                find_num(idx + 1, num_str + str(i))
                visited[i] = False

k = int(input())
ineqs = input().split()
visited = [False] * 10
result = []
find_num(0, '')

print(max(result))
print(min(result))