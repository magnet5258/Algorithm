from collections import Counter

word = input()
counter = Counter(word.upper())
most_common_list = counter.most_common()
max_count = most_common_list[0][1]
most_frequent = [char for char, count in most_common_list if count == max_count]
if len(most_frequent) > 1:
    print('?')
else:
    print(most_frequent[0])