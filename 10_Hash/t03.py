'''
파이선에서  tuple은 hash를 지원
tuple(튜플)은 불변한 순서가 있는 객체의 집합입니다.
list형과 비슷하지만 한 번 생성되면 값을 변경할 수 없습니다.
'''
def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1


clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
solution(clothes)