def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                plus_num = numbers[i] + numbers[j]
                if plus_num not in answer:
                    answer.append(plus_num)
    return sorted(answer)