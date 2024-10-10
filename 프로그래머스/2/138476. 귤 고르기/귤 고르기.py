from collections import Counter

def solution(k, tangerine):
    count = Counter(tangerine)
    sorted_count = count.most_common()
    answer = 0
    for i in range(len(sorted_count)):
        if k > 0:
            k -= sorted_count[i][1]
            answer += 1
    return answer