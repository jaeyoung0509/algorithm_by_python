d = [0] * 3000
def solution(n):
    for i in range(2 , n+1):
        d[i] = d[i-1] + 1
        print(i,  d[i])
        if i % 2 == 0 :
            d[i] = min(d[i] , d[i //2 ] +1)
            print(i,' % 2 == 0 ' , d[i] , d[i//2])
        if i % 3 == 0 :
            d[i] = min(d[i] , d[i //3 ] +1)
            print(i, ' % 3 == 0 ' , d[i] , d[i//3])

            
        if i % 5 == 0 :
            d[i] = min(d[i] , d[i //5 ] +1)  
            print(i,  '% 5 == 0 ' , d[i] , d[i//5])

    return d[i]


print(solution(26))

