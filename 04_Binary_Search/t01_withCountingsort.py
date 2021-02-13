#순차탐색 sequential_search

def solution(n, m):
    array =  [0] * (max(n)+1)
    for i in n :
        array[i] = 1
    for j in m:
        print(j)
        if array[j] == 1:
            return j
        else:
            return None

n = [8 , 3, 7 , 5, 2]
m = [5 , 7 ,9]
n.sort()
print(solution(n, m))