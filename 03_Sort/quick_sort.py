'''
퀵 정렬 
기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
pivot 값보다 왼쪽은 작고 오른쪽은 크고  이러한 작업을 divide or partition으로 부름
퀵 정렬을 재귀적으로 진행  너비는 n 높이는 logn nlogn , 최악은 n2
'''
array = [ 7,  5 , 9 ,0 , 3 , 1 ,6 ,2 ,4 ,8]
def quick_sort(array, start, end):

    if start >=end : #원소가 한 개 인 경우
        return
    pivot =  start   
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[pivot] >= array[left]:
            left += 1
        while right > start and array[pivot] <= array[right]:
            right -= 1
        if left > right:
            array[right] , array[pivot] = array[pivot] , array[right]
        else :
            array[left] , array[right] = array[right] , array[left]
    print("q: " , left , right ,start)
    quick_sort(array , start , right -1 )
    quick_sort(array , right+1 , end)

quick_sort(array , 0 , len(array) -1)
print(array)