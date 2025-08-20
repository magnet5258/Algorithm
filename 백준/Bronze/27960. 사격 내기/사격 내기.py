score_lst = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]

SA, SB = map(int, input().split())

SC = 0
for score in score_lst:
    if SA >= score and SB >= score:
        SA -= score
        SB -= score
    elif SA < score <= SB:
        SC += score
        SB -= score
    elif SB < score <= SA:
        SC += score
        SA -= score
    else:
        continue

print(SC)