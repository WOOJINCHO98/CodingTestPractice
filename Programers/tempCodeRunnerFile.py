def solution(d, budget):
    answer = 0
    
    d.sort()
    print(d)
    i = 0
    
    for i in range(len(d)):

        if d[i] <= budget:
            budget -= d[i]
            answer += 1
        else:
            break
    
    print(answer)
    return answer