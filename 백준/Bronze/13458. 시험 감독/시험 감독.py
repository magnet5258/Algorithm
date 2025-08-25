N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

total = 0
for i in A:
    total += 1
    if i <= B:
        continue
    else:
        if (i - B) % C == 0:
            total += (i - B) // C
        else:
            total += (i - B) // C + 1

print(total)