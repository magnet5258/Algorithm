def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i, price in enumerate(prices):
        while stack and stack[-1][1] > price:
            past_i, past_price = stack.pop()
            answer[past_i] = i - past_i
        stack.append((i, price))    
    
    while stack:
        past_i, past_price = stack.pop()
        answer[past_i] = len(prices) - 1 - past_i
    
    return answer