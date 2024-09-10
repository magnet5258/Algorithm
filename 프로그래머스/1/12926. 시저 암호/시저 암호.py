def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if 'A' <= s[i] <= 'Z':
            answer += chr(ord('A') + (ord(s[i]) - ord('A') + n) % 26)
        elif 'a' <= s[i] <= 'z':
            answer += chr(ord('a') + (ord(s[i]) - ord('a') + n) % 26)
        else:
            answer += s[i]
    return answer