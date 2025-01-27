num_lst = [-1] * 26
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
S = input()
for i, char in enumerate(S):
    if num_lst[alphabet.index(char)] == -1:
        num_lst[alphabet.index(char)] = i
print(' '.join(map(str, num_lst)))