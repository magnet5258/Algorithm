num_dic = {'ABC': 3, 'DEF': 4, 'GHI': 5, 'JKL': 6, 'MNO': 7, 'PQRS': 8, 'TUV': 9, 'WXYZ': 10}
word = input()
ans = 0
for i in word:
    for key in num_dic:
        if i in key:
            ans += num_dic[key]
print(ans)