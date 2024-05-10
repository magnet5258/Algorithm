def solution(n_str):
    answer = list(n_str)
    for i in answer[:]:
        if i == "0":
            answer.remove(i)
        else:
            break
    return ''.join(answer)