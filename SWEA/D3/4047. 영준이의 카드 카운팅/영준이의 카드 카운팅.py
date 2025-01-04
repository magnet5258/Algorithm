T = int(input())
for test_case in range(1, T + 1):
    card = input()
    card_dic = {'S' : 13, 'D' : 13, 'H' : 13, 'C' : 13}
    card_lst = [card[i:i+3] for i in range(0, len(card), 3)]
    check_lst = []
    ans = ""
    for i in card_lst:
        if i in check_lst:
            ans = 'ERROR'
        else:
            check_lst.append(i)
            if i[0] in card_dic:
                card_dic[i[0]] -= 1
    if ans != 'ERROR':
        ans = " ".join(map(str, card_dic.values()))
    print(f'#{test_case} {ans}')