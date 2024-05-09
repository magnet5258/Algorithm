def solution(myStr):
    for i in range(0, len(myStr)):
        if myStr[i] == "a":
            myStr = myStr.replace(myStr[i], " ")
        elif myStr[i] == "b":
            myStr = myStr.replace(myStr[i], " ")
        elif myStr[i] == "c":
            myStr = myStr.replace(myStr[i], " ")
    answer = myStr.strip().split()
    return answer if answer else ["EMPTY"]