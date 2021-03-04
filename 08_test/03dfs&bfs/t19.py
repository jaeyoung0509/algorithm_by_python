#연산자 끼어넣기
nums = [1 ,2 , 3 , 4, 5, 6]
add , sub , mul , div =   2, 1, 1, 1
#seperate[0] :+ 의 갯수 , sep[1] : - , sep[2] : x , sep[3] : %
n = len(nums)
max_ , min_ = 1e9 , -1e9


def dfs(i ,now , add ,sub ,mul ,div):
    global max_ , min_
    if i == n:
        max_ = max(now ,max_)
        min_ = min(now ,min_)
        return
    else:
        if add:
            dfs(i+1 , now+data[i] , add -1 , sub ,mul , div)
        if sub:
            dfs(i+1 , now-data[i] , add , sub - 1 , mul ,div)
        if mul:
            dfs(i+1 , now * data[i] , add , sub , mul- 1 ,div)
        if div:
            dfs(i+1 , int(now / data[i]) , add , sub , mul, div-1 )
    
dfs(1 , data[0] ,add, sub , mul , div)
print(max_)
print(min_)