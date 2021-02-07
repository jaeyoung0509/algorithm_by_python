def soulution(n , m , k , data):
    # n : 데이터 개수 , m : 숫자가 더해지는 횟수 , k : 특정 인덱스가 k번까지만 더 해질 수 있음
    m1 , k1 = m  , k
    answer = 0
    data.sort(reverse=True)
    while( m1 > 0 ):
        for _ in range(k):
            answer += data[0]
            m1 -= 1
            if(m1 == 0):
                break
        if m1 == 0:
            break
        else:
            answer += data[1]
            m1 -= 1
    return answer
# n, m ,k =  map( int , input().split())
# data = list(map (int , input().split()))
n , m , k = 5 , 8, 3
data = [2 , 4 ,5 ,4, 6]
sol = soulution(n , m , k , data)
print(sol)