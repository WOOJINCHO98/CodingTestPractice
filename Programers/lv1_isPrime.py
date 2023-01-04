def is_prime(n):
    temp = 0
    for i in range (2,n-1):
        if n%i == 0:
            temp = 0
            break
        else:
            temp = 1
    
    if n == 2 or n==3:
        temp = 1
        
    print(temp)
    return temp

def solution(n):
    answer = 0

    for i in range(1, n+1):
        if(is_prime(i)):
            answer += 1
    print(answer)
    return answer

solution(15)
print("----")
solution(10)
print("----")
solution(5)
