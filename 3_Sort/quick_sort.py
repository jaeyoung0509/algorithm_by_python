'''
퀵 정렬 
기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
pivot 값보다 왼쪽은 작고 오른쪽은 크고  이러한 작업을 divide or partition으로 부름
퀵 정렬을 재귀적으로 진행  너비는 n 높이는 logn nlogn , 최악은 n2
'''
array = [ 7,  5 , 9 ,0 , 3 , 1 ,6 ,2 ,4 ,8]
def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복 
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

#간단하게
def quick_sort2(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:] #pivot을 제외한 리스트
    left_side = [ x for x in tail if x<= pivot]
    right_side = [ x for x in tail if x > pivot]
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

quick_sort(array, 0, len(array) - 1)
print(quick_sort2(array))