N = int(input())
cnt = 0
num = 665
while True:
    if '666' in str(num):
        cnt += 1
        if cnt == N:
            print(num)
            break
    num += 1