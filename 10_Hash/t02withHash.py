def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp!= phone_number:
                answer = False
    return True

a= ["11" , "222221111" ,"33" ,"444" , "22"]
print(solution(a))