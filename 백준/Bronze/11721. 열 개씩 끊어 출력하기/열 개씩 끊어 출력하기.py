word = input()
i = 0
while i < len(word):
    if i + 10 < len(word):
        print(word[i:i + 10])
    else:
        print(word[i:])
    i += 10