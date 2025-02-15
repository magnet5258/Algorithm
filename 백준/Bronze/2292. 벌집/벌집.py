N = int(input())
num = 1
layer = 1
if N > 1:
    while num < N:
        num += 6 * layer
        layer += 1
print(layer)