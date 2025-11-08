from itertools import permutations

def solution(k, dungeons):
    answer = 0
    perm = list(permutations(dungeons))
    for lst in perm:
        num = k
        cnt = 0
        for a, b in lst:
            if num >= a:
                cnt += 1
                num -= b
        answer = max(answer, cnt)
    return answer