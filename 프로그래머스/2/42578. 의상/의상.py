from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(int)
    for name, types in clothes:
        clothes_dict[types] += 1
    answer = 1
    for key, value in clothes_dict.items():
        answer *= value + 1
    return answer - 1