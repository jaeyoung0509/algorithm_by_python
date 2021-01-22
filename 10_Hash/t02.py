#lambda
#sort(key) 
#sort vs sorted
#sort는 반환값이 없음 , sorted 있음
def solution(phone_book):
    phone_book.sort(key = lambda x :len(x))
    print( phone_book)
    #print(phone_book[4][:len(phone_book[2])])
    for i in range(len(phone_book)):
        for j in range(i+1 , len(phone_book)):
            if phone_book[j][:len(phone_book[i])] == phone_book[i]:
                print(phone_book[j] , i ,j)
                return False
    return True
a= ["11" , "222221111" ,"33" ,"444" , "22"]
print(solution(a))