'''
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
'''

def solution(clothes):
    answer = 1
    list_ = []
    kind_clothes = dict()
    for i in clothes:
        if i[1] not in kind_clothes :
            kind_clothes[i[1]] = [i[0]]
        else:
            kind_clothes[i[1]].append(i[0])
    clothes_idx = kind_clothes.keys()
    for i in clothes_idx:
        list_.append(len(kind_clothes[i]))
    
    for i in list_:
        answer *= (i+1)
        
    return answer -1



clothes  = 	[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
a = solution(clothes)
print(a)