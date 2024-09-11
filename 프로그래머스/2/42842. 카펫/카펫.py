def solution(brown, yellow):
    n = int((brown - 4) / 2)
    for i in range(1, n):
        if i * (n - i) % yellow == 0:
            width = n - i + 2
            height = i + 2
            break
    return [width, height]