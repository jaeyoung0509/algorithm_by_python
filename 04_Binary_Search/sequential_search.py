#순차탐색 sequential_search

def sequential_search( n  ,target ,array):
    for i in range(n):
        if array[i] == target:
            return i+1
array = ["ㅋ" , "ㅎ" , "ㅈ"]

print(sequential_search(len(array) , "ㅎ" , array))