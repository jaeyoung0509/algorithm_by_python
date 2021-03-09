def solution(m , load):
    load.sort()
    trucks = 0
    start = 0
    last = len(load) -1
    sum_ = 0
    while start <= last:
        sum_ += load[start] + load[last]
        if sum_ > m:
            last -=1
            sum_ = 0
        if sum == m:
            last -= 1
            start += 1
            sum_ =0
        else:
            start += 1
            last -=1 
        trucks += 1
    return trucks



m = 10
load =    [2,3,7,8] 
a = solution(m, load)
print("zzzzzzzz", a)