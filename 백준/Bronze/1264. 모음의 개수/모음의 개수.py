while True:
    sentence = input()
    if sentence == '#':
        break
    cnt = sum(1 for i in sentence if i in 'aeiouAEIOU')
    print(cnt)