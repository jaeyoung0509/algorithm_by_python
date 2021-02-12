'''
퀵 정렬 
기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
pivot 값보다 왼쪽은 작고 오른쪽은 크고  이러한 작업을 divide or partition으로 부름
퀵 정렬을 재귀적으로 진행  너비는 n 높이는 logn nlogn , 최악은 n2
'''
array = [ 7,  5 , 9 ,0 , 3 , 1 ,6 ,2 ,4 ,8]
def quick_sort(array):
    if len(array) <= 1:
        print("zxzzzzzzzzzzzzzzzzzzzzz" ,array)
        return array
    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x<= pivot]
    right_side =[x for x in tail if x > pivot]
    print(array ,left_side , right_side)

    return(quick_sort(left_side) + [pivot] + quick_sort(right_side))

print(quick_sort(array))