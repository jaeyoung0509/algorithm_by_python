def solution(numbers):
    ans= ""
    temp = numbers
    temp.sort(reverse= True)
    answer = []
    for i in temp:
        t = i
        cnt = 0
        while(t>0):
            t = int(t/10)
            cnt += 1
        answer.append([i ,cnt])
    for i in range(len(answer)):
        answer[i].append(int(answer[i][0]) * 10 ** int(answer[0][1] - answer[i][1]) )   
    answer.sort(key= lambda x :( x[2] , -x[0] ), reverse= True)
    print(answer)
    for i in answer:
        ans= ans + str(i[0])
    return ans

numbers = [100 , 3 , 30 ,3 ,3]
print(solution(numbers))
