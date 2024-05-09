def solution(myString, pat):
    a = myString.lower()
    b = pat.lower()
    if b in a:
        return 1
    else:
        return 0