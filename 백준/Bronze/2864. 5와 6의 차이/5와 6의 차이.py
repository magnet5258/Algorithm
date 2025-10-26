A, B = input().split()

sA = ''
lA = ''
sB = ''
lB = ''
for i in range(len(A)):
    if A[i] == '6':
        sA += '5'
        lA += A[i]
    elif A[i] == '5':
        sA += A[i]
        lA += '6'
    else:
        sA += A[i]
        lA += A[i]

for i in range(len(B)):
    if B[i] == '6':
        sB += '5'
        lB += B[i]
    elif B[i] == '5':
        sB += B[i]
        lB += '6'
    else:
        sB += B[i]
        lB += B[i]

print(int(sA) + int(sB), int(lA) + int(lB))