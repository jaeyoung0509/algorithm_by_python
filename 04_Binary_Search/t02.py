def solution(n ,array):
    result = []
    start = 0
    array.sort()
    end = max(array)
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for i in array:
            if i >= mid :
                total = total + i -mid
        if total < n:
            end = mid -1
        elif total >= n :
            start = mid + 1
            result.append(mid)
    print(result)
    return max(result)
            



n= 6
array = [19 , 15 , 10 , 17]
print(solution(n , array))