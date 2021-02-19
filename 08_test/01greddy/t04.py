def solution(lists):
    answer = 0
    for i in range(len(lists)):
        for j in range(i+1 , len(lists)):
            if i != j and lists[i] != lists[j]:
                print(lists[i] , lists[j])
                answer+=1
        
    return answer

lists = [1, 5 , 4 , 3, 2, 4, 5, 2]
print(solution(lists))