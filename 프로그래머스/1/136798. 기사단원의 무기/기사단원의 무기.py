def solution(number, limit, power):
    answer = 0
    divisors = [0] * (number + 1)
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            divisors[j] += 1
    for i in range(1, number + 1):
        if divisors[i] > limit:
            answer += power
        else:
            answer += divisors[i]
    return answer