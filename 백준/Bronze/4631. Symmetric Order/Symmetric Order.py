case = 1

while True:
    num = int(input())
    if num == 0:
        break
    else:
        names = list(input() for _ in range(num))
        order = []
        for i in range(0, len(names), 2):
            order.append(names[i])
        if num % 2 == 0:
            for j in range(len(names) - 1, -1, -2):
                order.append(names[j])
        else:
            for j in range(len(names) - 2, -1, -2):
                order.append(names[j])
        print(f'SET {case}')
        for name in order:
            print(name)

        case += 1