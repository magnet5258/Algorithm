def solution(citations):
    sorted_ct = sorted(citations, reverse=True)
    for i in range(len(citations)):
        if sorted_ct[i] < i + 1:
            return i
    return len(citations)