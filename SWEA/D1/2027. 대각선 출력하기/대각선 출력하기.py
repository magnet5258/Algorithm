for i in range(5):
    ans = '+' * 5
    ans = ans[:i] + '#' + ans[i + 1:]
    print(ans)