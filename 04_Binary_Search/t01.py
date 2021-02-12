#순차탐색 sequential_search

def solution(target , start , end ,array):
    array.sort()
    while(start <= end):
        mid = (start + end) // 2
        if array[mid] == target:
            print("hh", array[mid])
            return mid
        elif array[mid] < target:
            end = mid -1
        else:
            start = mid + 1
        return None

n = [8 , 3, 7 , 9, 2]
m = [5 , 7 ,9]
for i in m :
    print(i)
    if solution(i , 0 ,len(n)-1 , n) is not None:
        print(i , "is  exsisted")
    
