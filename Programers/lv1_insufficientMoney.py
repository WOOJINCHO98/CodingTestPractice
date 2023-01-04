def solution(price, money, count):
    answer = -1
    
    for i in range(1,count+1):
        money = money - price * i

    if money<0:
        answer = -1*money
        
    else:
        answer = 0
        
    return answer