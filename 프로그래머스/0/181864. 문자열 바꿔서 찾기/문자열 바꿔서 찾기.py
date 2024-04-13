def solution(myString, pat):
    a = list(myString)
    for i in range(len(a)):
        if a[i] == "A":
            a[i] = "B"
        else:
            a[i] = "A"
    b = ''.join(a)
    if pat in b:
        return 1
    else:
        return 0