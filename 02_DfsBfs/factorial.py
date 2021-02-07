#반복문으로 
def factorial_iteraitve(n):
    result = 1
    for i in range(1 , n +1):
        result *= i
    return result

#재귀표현으로
def factorail_recursive(n):
    if n<= 1:
        return 1
    print(n, '입니다')
    return n * factorail    _recursive(n-1)

print(factorail_recursive(5))