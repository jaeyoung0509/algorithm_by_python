def solution(numbers):
        numbers = list(map(str, numbers))
        numbers_list = []
        answer = ""
        for i in numbers:
            tmp = i
            if  int(tmp) < 10:
                tmp = tmp * 12
            if 10 <= int(tmp) < 100:
                tmp = tmp * 6
            if 100<= int(tmp) <1000:
                tmp = tmp * 4
            if int(tmp) >= 1000:
                tmp = tmp * 3
            numbers_list.append((int(tmp) ,int(i)))
        numbers_list.sort(key = lambda x: (-x[0] , x[1]))
        return ''.join([str(number[1]) for number in numbers_list])
        

numbers = [21 , 212]
print(solution(numbers))

#reutn 6210