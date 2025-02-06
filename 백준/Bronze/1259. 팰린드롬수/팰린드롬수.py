while True:
    num = input()
    ans = 'yes'
    if num == '0':
        break
    else:
        for i in range(len(num) // 2):
            if num[i] != num[len(num) - 1 - i]:
                ans = 'no'
                break
    print(ans)