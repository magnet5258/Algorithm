while True:
    s_list = list(map(int, input().split()))
    n = s_list[0]
    if n == 0:
        break
    hist = s_list[1:]
    stack = []
    max_area = 0
    idx = 0
    
    while idx < n:
        if not stack or hist[stack[-1]] <= hist[idx]:
            stack.append(idx)
            idx += 1
        else:
            top = stack.pop()
            width = idx if not stack else idx - stack[-1] - 1
            max_area = max(max_area, hist[top] * width)

    while stack:
        top = stack.pop()
        width = idx if not stack else idx - stack[-1] - 1
        max_area = max(max_area, hist[top] * width)

    print(max_area)