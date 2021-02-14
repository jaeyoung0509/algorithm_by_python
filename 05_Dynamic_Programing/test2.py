def solution(n):
    answer = 0
    d = [0] * 100
    d[0] = n[0]
    d[1] = max(n[0] , n[1]) 
    for i in range(2 , k):
        d[i] = max(d[i-1]  ,d[i -2 ]+ n[i])  
    return answer


n = [1 ,3 , 1,5]
solution(n)



