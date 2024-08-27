def solution(price, money, count):
    price_sum = 0
    
    for i in range(1, count + 1):
        price_sum += price * i
        
    if money > price_sum:
        return 0
    else:
        return abs(money - price_sum)