a, b, c = map(int, input().split())
if a == b and b == c:
    cnt = 3
    num = 10000 + a * 1000
elif a == b or a == c:
    cnt = 1
    num = 1000 + a * 100
elif b == c:
    cnt = 1
    num = 1000 + b * 100
else:
    cnt = 0
    num = max(a, b, c) * 100
    
print(num)