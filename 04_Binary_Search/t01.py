#순차탐색 sequential_search

def solution(target , start , end ,array):
    while(start <= end):
        mid = (start + end) // 2
        print(mid , start ,end , array[mid])
        if array[mid] == target:
            return array[mid]
        elif array[mid] > target:
            end = mid -1
        elif array[mid] < target:
            start = mid + 1
    return None

n = [8 , 3, 7 , 5, 2]
m = [5 , 7 ,9]
n.sort()
for i in m :
    t = solution(i , 0 ,len(n)-1 ,n)
    print(t)
    if t==i:
        print(i , "is  exsisted")
    
