N = int(input())
measure = sorted(list(map(int, input().split())))
print(measure[0] * measure[-1])