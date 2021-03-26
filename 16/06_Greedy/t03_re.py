def solution(number, k):
    num = list(number)
    count = 0
    idx = len(num) - k+1
    while idx < len(num) :
        remove_point = num.index(min(num[-idx]))
        print(num[:idx] , num[remove_point])
        if remove_point ==0 :
            num = num[1:]
            count += 1
            print("aaa",num)

        if remove_point >= 1:
            print(num , num[remove_point])
            num.remove(num[remove_point])
            count += remove_point
            print(num)
    return ''.join([str(i) for i in num])
    



number= "1942"
k = 3
a = solution(number, k)
print(a)