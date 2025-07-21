import math

w, h = map(int, input().split())
cal_1 = w + h
cal_2 = math.sqrt(w ** 2 + h ** 2)
answer = cal_1 - cal_2

if answer.is_integer():
    print(int(answer))
else:
    print(round(answer, 9))