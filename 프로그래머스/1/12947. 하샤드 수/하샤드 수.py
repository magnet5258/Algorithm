def solution(x):
    a = 0
    s = str(x)
    for i in range(len(s)):
        a += int(s[i])
    if x % a == 0:
        return True
    else:
        return False