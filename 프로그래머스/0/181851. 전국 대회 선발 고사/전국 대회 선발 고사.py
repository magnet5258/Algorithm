def solution(rank, attendance):
    x = []
    for i in range(len(attendance)):
        if attendance[i] == True:
            x.append(rank[i])
    x.sort()
    answer = rank.index(x[0])*10000 + rank.index(x[1])*100 + rank.index(x[2])
    return answer