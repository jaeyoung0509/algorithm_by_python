def count_by_value(array , x):

    n = len(array)

    a = first(array ,x , 0 , n-1)
    print(a)
    if a == None:
        print("zz")
        return 0 
    b = last(array ,x ,0 , n-1)
    if b == None:
        print("cc")
        return 0
    print( a, b)
    return int(b)-int(a)+1

def first(arry , target , start, end):
    if start > end:
        return None
    mid = (start + end) //2

    if (mid == 0 or target > array[mid-1]) and  array[mid] == target:
        return mid

    elif array[mid] > target:
        # target보다 값이 클때 -> 범위를 left로 줄이기
        return first(array , target , start , mid- 1)
    
    elif arry[mid] < target:
        return first(array , target ,mid +1 , end)

    
def last(array , target , start , end):
    mid = (start + end) //2
    if start > end:
        return None
    if(mid == len(array) -1 or  target < array[mid +1]) and array[mid] == target:
        print("zzzzzzzzzzzz")
        return mid
    elif array[mid] > target:
        return last(array ,target ,start , mid -1)
    elif array [mid] < target:  
        return last(array , target , mid+1 , end)


array = [1 , 1 ,  2 , 2 , 3 ]
count = count_by_value(array ,2)
print(count)