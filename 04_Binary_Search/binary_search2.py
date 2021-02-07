'''
순차탐색: 리스트 안에 잇는 특정한 데이터를 찾기위해 앞에서 부터
이진탐색: 정렬되어 있는 리스트에서 특정 범위를 절반씩 좁혀가며  데이터를 탐색하는 방법
-이진탐색은 시작점 ,끝점 ,중간점을 이용하여 탐색범위를 설정합니다. -> O(LOGn)시간의 복잡도를 가짐
라이브러리 bisect_left( a  ,x)
라이브러리 bisect_right(a ,x )
'''
#bisect를 이용해 값이 특정 범위에 속하는 데이터 개수를 구하기
from bisect import bisect_left , bisect_right

def count_by_range(a , left_value , right_value):
    right_index =bisect_right( a , right_value)
    left_index =bisect_left( a, left_value)
    return right_index - left_index

a = [ 1 , 2, 3 , 4 ,5 ,6 , 7 ,8 ,9]
print(count_by_range(a ,4, 4))
print(count_by_range(a , -1 ,3))
