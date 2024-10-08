def solution(name, yearning, photo):
    answer = []
    name_dict = dict(zip(name, yearning))
    for i in range(len(photo)):
        result = 0
        for j in photo[i]:
            if j in name:
                result += (name_dict[j])
        answer.append(result)
    return answer