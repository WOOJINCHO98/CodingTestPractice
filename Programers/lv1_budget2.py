# Runtime Error

def solution(d, budget):
    answer = 0
        
    print(d)
    i = 0
    while budget > 0:
        temp = min(d)
        d.remove(temp)
        budget -= temp
        i += 1
        print(budget)
    
    answer = i-1
    if budget == 0:
        answer += 1
    print(answer)
    return answer

solution([1,3,2,5,4], 9)
solution([2,2,3,3], 10)