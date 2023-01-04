
def solution(n):
    answer = 0
    
    temp = []
    
    for i in range(1,n):
        if n%i==0:
            temp.append(i)

    print(temp)
    return answer

solution(10)