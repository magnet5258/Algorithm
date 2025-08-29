total = 0
for _ in range(10):
    mushroom = int(input())
    if total + mushroom <= 100:
        total += mushroom
    else:
        if total + mushroom - 100 <= 100 - total:
            total += mushroom
            break
        else:
            break

print(total)