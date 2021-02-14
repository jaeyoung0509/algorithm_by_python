d = [0] * 100
def solution(x):
    if x==1 or x==2:
        return 1
    if d[x] !=0 :
        return d[x]
    d[x] = solution(x-1) + solution(x-2)
    return d[x]

print(solution(20))