def solution(number):
    answer = 0
    
    #배열중 3가지 뽑는다. 그 3명의 합이 0 이면 answer +1

    for i in range(len(number)):
        for j in range(i+1,len(number)):
            for k in range(j+1,len(number)):
                if number[i]+number[j]+number[k] == 0:
                    answer += 1
    
    return answer