def solution(numbers):
        numbers_list = []
        answer = ""
        for i in numbers:
            tmp = str(i)
            tmp2 = "1000"
            if  i < 1000:
                tmp2 = ""
            if 10 <= int(tmp)*10  < 100: #한자릿수 
                tmp2 = tmp + "000"
                tmp = tmp *4
            if 100 <= int(tmp) *10 < 1000: #두자릿수
                tmp2 = tmp + "00"
                tmp = tmp * 2
            if 100 <= int(tmp)  < 1000:#세자릿수
                tmp2 = tmp + "0"  
                tmp = int(tmp) * 10
            if int(tmp) != 0: 
                numbers_list.append([i, int(tmp) , int(tmp2)])
            else:
                numbers_list.append([0 , 0, 0])
        numbers_list.sort(key = lambda x: (-x[2], x[0] , -x[1]))
        #print(numbers_list)
        return str(int(''.join([str(number[0]) for number in numbers_list])))



numbers = [21 , 212]
print(solution(numbers))

#reutn 6210