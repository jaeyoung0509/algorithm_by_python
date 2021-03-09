def solution(m , load):
    if (max(load) > 40 or min(load) <1 or  max(load) > m) :
        return -1
    n  ,trucks = len(load)-1  , 0
    load.sort()
    while len(load) > 0:
        if len (load) == 1:
            return trucks + 1
        tmp_a , tmp_b = load[0] , load[n]
        sum_ = tmp_a + tmp_b
        if (sum_  < m):
            while( sum_ < m):
                del load[0]
                tmp_a = load[0]
                sum_ += tmp_a
                if sum_ < m:
                    trucks+=1
        if (sum_ >= m):
            print(n)
            del load[0]
            n -= 1
        
    return trucks



m = 5 
load =    [2,2,2,2,2]
a = solution(m, load)
print("zzzzzzzz", a)