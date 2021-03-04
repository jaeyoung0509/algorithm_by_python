def binary_search(data , start, end):
    if start > end:
        return -1
    mid = (start + end) // 2

    if data[mid] == mid :
        return mid
    
    elif data[mid] > mid:
        return binary_search(data , start , mid- 1)

    elif data[mid] < mid:
        return binary_search(data , mid +1 , end)


index= binary_search(data , 0 , len(data-1))