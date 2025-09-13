N, r, c = map(int, input().split())
result = 0
size = 2 ** N

while size > 1:
    size //= 2
    half = size ** 2
    if r < size and c < size:
        pass
    elif r < size and c >= size:
        result += half
        c -= size
    elif r >= size and c < size:
        result += half * 2
        r -= size
    else:
        result += half * 3
        r -= size
        c -= size

print(result)