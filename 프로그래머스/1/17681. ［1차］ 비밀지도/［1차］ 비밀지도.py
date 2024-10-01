def solution(n, arr1, arr2):
    bin_arr1 = [bin(i)[2:].zfill(n) for i in arr1]
    bin_arr2 = [bin(j)[2:].zfill(n) for j in arr2]

    answer = []
    for b1, b2 in zip(bin_arr1, bin_arr2):
        new_answer = ''.join(' ' if x == '0' and y == '0' else '#' for x, y in zip(b1, b2))
        answer.append(new_answer)
    
    return answer