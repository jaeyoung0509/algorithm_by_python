from collections import deque
import copy
def solution(progresses, speeds):
    list_ = []
    answer = []
    sol = []
    for i in range(len(progresses)):
        list_.append((progresses[i] , speeds[i]))
    q = deque(list_)
    while q :
        p , s = q.popleft()
        count = 1
        while ((p+(s* count))  < 100):
            count += 1
        answer.append(count)
    #---------걸리는 시간 구하기 [ 5 , 10 , 1, 1, 20, 1]-----------
    ans_q = deque(answer)
    while len(ans_q) > 0 :
        tmp = ans_q.popleft()
        cnt = 1
        for i in copy.deepcopy(ans_q):
            if tmp < i:
                break
            ans_q.popleft()
            cnt += 1
        sol.append(cnt)
    return sol

               
progresses = [95, 90, 99, 99, 80, 99]
speeds =  [1, 1, 1, 1, 1, 1]
t =  solution(progresses , speeds)
print(t)