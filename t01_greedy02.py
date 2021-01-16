n = int(input())
k = int(input())
result  = 0

while True:
    target = ( n // k)  * k   # // -> 몫을 구하는 거임 !   더하기
    result  += (n - target)
    n = target
    if n < k :
        break
    result += 1
    n // k

result += (n-1)
print(result)