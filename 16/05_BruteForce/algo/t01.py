from collections import deque
def solution(m , load):
    if (max(load) > 40 or min(load) <1 or  max(load) > m) :
        return -1
    load.sort()
    q_a = deque(sorted(load))
    while q_a:
        if len(q_a) >= 2:
            tmp_a , tmp_b = q_a.pop() , q_a.popleft()
            sum_= tmp_a + tmp_b
            sum_ = tmp_a + tmp_b
            if sum_ < m:
                while sum_ < m:
                    tmp_a = q_a.pop()
                sum_ += tmp_a
                if sum_ > m:
                    q_a.append(tmp_a)
                else:
                    trucks+=1
    return trucks



m = 5 
load =    [2,2,2,2,2]
a = solution(m, load)
print("zzzzzzzz", a)