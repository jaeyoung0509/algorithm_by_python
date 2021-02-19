def solution(k):
    result = 0
    count = 0
    while(count < len(k)):
        a  = int(k[count])
        if (a <= 1):
            result += a 
        else:
            if result == 0:
                result += a
            else:
                result = result * a
        count+=1

    return result


k = '02984'
print(solution( k))