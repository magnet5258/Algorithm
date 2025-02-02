N = int(input())
lst = []
for i in range(N):
    word = input()
    lst.append(word)
group = 0
for word in lst:
    word_set = set(word)
    cnt = 0
    for j in word_set:
        num = 1
        for k in range(len(word) - 1):
            if word[k] == j and word[k + 1] == j:
                num += 1
        if word.count(j) == num:
            cnt += 1
    if cnt == len(word_set):
        group += 1
print(group)
