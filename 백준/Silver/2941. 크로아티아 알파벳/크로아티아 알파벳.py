croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
cnt = 0
for a in croatia:
    cnt += word.count(a)
    word = word.replace(a, ' ')
word = word.replace('-', '').replace('=', '').replace(' ', '')
cnt += len(word)
print(cnt)