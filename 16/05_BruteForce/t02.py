from itertools import permutations
def solution(numbers):
    #순열 함수 외우기
    answer = []
    for k in range(1 , len(numbers)+1):
        prelist = list(map(''.join, permutations(list(numbers) , k)))
        for i in list(set(prelist)):
            if prime_number(int(i)) and int(i) not in answer:
                answer.append(int(i))
    print(answer)
    return len(answer)
def prime_number(num):
    ans = []
    count = 1
    for i in range(1 , num//2 +1):
        if num % i == 0:
            count +=1
        if count > 2:
            return False
    if count == 2:
        return True
numbers ="011"
a= solution(numbers)
print(a)
