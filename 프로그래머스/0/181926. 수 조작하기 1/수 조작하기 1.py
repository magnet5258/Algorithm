def solution(n, control):
    for x in range(len(control)):
        if control[x] == 'w':
            n += 1
        elif control[x] == 's':
            n -= 1
        elif control[x] == 'd':
            n += 10
        elif control[x] == 'a':
            n -= 10
    return n