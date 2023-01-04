
def solution(n, m):
    answer = []
    _n = []
    _m = []
    div = 0 # 최대공약수
    mul = 0 # 최소공배수

    if n>m:
        n, m = m ,n
    
    for i in range (1, n+1):
        if n%i == 0:
            _n.append(i)

    for i in range (1, m+1):
        if m%i == 0:
            _m.append(i)

    for i in _n:
        if i in _m:
            div = i
        
    mul = n*m/div

    answer.append(div)        
    answer.append(mul)    
            
    return answer



abc = [] 
abc = solution(3,12)