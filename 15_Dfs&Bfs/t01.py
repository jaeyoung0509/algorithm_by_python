from itertools import permutations

def solution(numbers):
    answer = 0
    lists = []
    for i in range(1 , len(numbers) +1):
        tmp = permutations(numbers , i)
    print(pemutes)
    return answer

def find_primeNumber(n):
    if n<=2:
        return False
    for i in range(2 ,n//2+1):
        if n% i == 0:
            return True
    return False



numbers = "17"
solution(numbers)