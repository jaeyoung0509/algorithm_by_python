'''
순차탐색: 리스트 안에 잇는 특정한 데이터를 찾기위해 앞에서 부터
이진탐색: 정렬되어 있는 리스트에서 특정 범위를 절반씩 좁혀가며  데이터를 탐색하는 방법
-이진탐색은 시작점 ,끝점 ,중간점을 이용하여 탐색범위를 설정합니다. -> LOG 시간의 복잡도를 가짐
'''
def binary_search(array , target , start , end):
    if start > end:
        return None
    mid = (start + end ) // 2
    if array[mid] == target:
        return mid
    if target > array[mid]:
        return binary_search(array ,target , mid + 1 , end)
    if target < array[mid]:
        return binary_search(array , target ,start , mid-1)


array = [ 0 , 2, 4 ,6 , 8 , 10 , 12 , 14 , 16 ,18]

target = 4

binary_search(array , target , 0  ,len(array)-1)