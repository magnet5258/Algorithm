N = int(input())
words = [input() for _ in range(N)]
sorted_words = sorted(set(words), key=lambda x: (len(x), x))
for word in sorted_words:
    print(word)