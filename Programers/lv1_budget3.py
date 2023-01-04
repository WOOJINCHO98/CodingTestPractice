def solution(d, budget):
    answer = 0
    
    d.sort()

    
    for i in range(len(d)):
        if d[i] <= budget:
            budget -= d[i]
            answer += 1
        else:
            break
    return answer

solution([1,3,2,5,4], 9)
solution([2,2,3,3], 10)