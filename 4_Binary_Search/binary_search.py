'''
순차탐색: 리스트 안에 잇는 특정한 데이터를 찾기위해 앞에서 부터
이진탐색: 정렬되어 있는 리스트에서 특정 범위를 절반씩 좁혀가며  데이터를 탐색하는 방법
-이진탐색은 시작점 ,끝점 ,중간점을 이용하여 탐색범위를 설정합니다. -> LOG 시간의 복잡도를 가짐
'''
 def binary_search(array , target , start , end):
     if start > end :
         return None
    mid = (start + end ) / 2
    if array[mid] == target:
        return mid
    #중간점의 값보다 찾고자 하는 값이 작을 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array , target , start , mid-1)
    #중간점의 값보다 찾고자 하는 값이 클 경우 
    elif array[mid] < target:
        return binary_search(array , target , mid +1 , end)


n , target = list (map( int , input().split()))

array = list ( map ( int , input().split()))

result = binary_search(array , target , 0 , n-1)
if result == None:
    print(" not found")
else :
    print(result +1)