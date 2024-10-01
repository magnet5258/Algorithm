def solution(n, arr1, arr2):
    answer = []
    bin_arr1 = []
    bin_arr2 = []
    for i in arr1:
        bin_arr1.append(bin(i)[2:].zfill(n))
    for j in arr2:
        bin_arr2.append(bin(j)[2:].zfill(n))
    for k in range(len(bin_arr1)):
        new_answer = ''
        for l in range(len(bin_arr1[k])):
            if bin_arr1[k][l] == '0' and bin_arr2[k][l] == '0':
                new_answer += '0'
            else:
                new_answer += '1'
        answer.append(new_answer)
    
    converted_answer = [''.join(map(lambda x: ' ' if x == '0' else '#', z)) for z in answer]
        
    return converted_answer