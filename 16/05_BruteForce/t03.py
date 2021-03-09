def solution(brown, yellow):
    answer = []
    all_ = brown + yellow
    for i in range(all_ , 2 , -1):
        if all_ % i ==0 :
            a = all_ // i
            s = (a-2) * (i-2)
            return ( a ,s)

brown = 10
yellow = 2
solution(brown, yellow)