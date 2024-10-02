def solution(k, score):
    answer = []
    k_list = []
    for i in range(len(score)):
        if len(k_list) <= k - 1:
            k_list.append(score[i])
        elif score[i] > min(k_list):
            k_list.remove(min(k_list))
            k_list.append(score[i])
        answer.append(min(k_list))    
    return answer