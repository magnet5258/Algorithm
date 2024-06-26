def solution(n):
    answer = [int(number) for number in str(n)]
    answer.sort(reverse = True)
    return int(''.join(map(str, answer)))