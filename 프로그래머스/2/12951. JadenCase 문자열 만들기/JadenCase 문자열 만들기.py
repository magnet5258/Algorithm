def solution(s):
    answer = ''
    cap = True
    for word in s:
        if word == ' ':
            answer += word
            cap = True
        elif cap and word.isalpha():
            answer += word.upper()
            cap = False
        else:
            answer += word.lower()
            cap = False
            
    return answer