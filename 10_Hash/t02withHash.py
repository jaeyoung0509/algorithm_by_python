def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    print(hash_map)
    return True

a= ["11" , "222221111" ,"33" ,"444" , "22"]
print(solution(a))