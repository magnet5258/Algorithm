T = int(input())
for t in range(1, T + 1):
    n = int(input())
    m = list(map(int, input().split()))
    
    max_right = [0] * n
    max_right[-1] = m[-1]
    for i in range(n - 2, -1 , -1):
        max_right[i] = max(max_right[i + 1], m[i + 1])
        
    answer = 0
    for i in range(n - 1):
        if m[i] < max_right[i]:
            answer += max_right[i] - m[i]
    print(f'#{t} {answer}')
            
                 
