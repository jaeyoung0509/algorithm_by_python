def solution(numbers):
    numbers = list(map(str, numbers))
    print(numbers)
    numbers.sort(key=lambda x: x*3, reverse=True)
    print(numbers)

    return str(int(''.join(numbers)))

numbers = [100 , 3 , 30 ,3 ,3 ,99]
print(solution(numbers))
