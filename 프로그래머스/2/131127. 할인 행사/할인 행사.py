def solution(want, number, discount):
    answer = 0
    want_lst = []
    for i in range(len(want)):
        want_lst += [want[i]] * number[i]
    want_lst.sort()
    length = len(want_lst)
    for i in range(len(discount) - length + 1):
        if want_lst == sorted(discount[i:i + length]):
            answer += 1
    return answer