def solution(absolutes, signs):
    sum = 0
    for i in range (len(signs)):
        if signs[i]==1:
            sum += absolutes[i]
        elif signs[i]==0:
            sum -= absolutes[i]            
    return sum

