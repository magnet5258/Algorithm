N = int(input())
X = list(map(int, input().split()))
sorted_X = list(set(sorted(X)))
dict_X = {}

for i in range(len(sorted_X)):
    dict_X[sorted_X[i]] = i

for num in X:
    print(dict_X[num], end=' ')