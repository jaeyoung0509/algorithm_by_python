#연산자 끼어넣기
nums = [5, 6]
add , sub , mul , div =   0 , 0 , 1 ,0
#seperate[0] :+ 의 갯수 , sep[1] : - , sep[2] : x , sep[3] : %
n = len(nums)
max_ , min_ = 1e9 , -1e9



def dfs(i, res, add, sub, mul, div):
    global max_, min_
    if i == n:
        max_ = max(res, max_)
        min_ = min(res, min_)
        return

    else:
        if add:
            dfs(i+1, res+nums[i], add-1, sub, mul, div)
        if sub:
            dfs(i+1, res-nums[i], add, sub-1, mul, div)
        if mul:
            dfs(i+1, res*nums[i], add, sub, mul-1, div)
        if div:
            dfs(i+1, int(res/nums[i]), add, sub, mul, div-1)

dfs(1, nums[0], add, sub, mul, div)
print(max_)
print(min_)
