def solution(data):
    sum0 , sum1 =  0 , 0
    for i in range(len(data)//2):
        sum0 += i
    for i in range(len(data)//2 , len(data)):
        sum1 += i
    if (sum0 == sum1):
        return 'LUCKY'
    else:
        return 'READY'

data = [123402]
print(solution(data))