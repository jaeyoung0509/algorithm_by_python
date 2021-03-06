import heapq
from collections import deque
def solution(jobs):
    tmp = []
    for x, y in jobs:
        tmp.append((y,x))
    tasks = deque(sorted(tmp , key = lambda x:x[0]))
    hq = []
    heapq.heappush(hq , tasks.popleft()) #첫번째 task를 hq에 넣음
    current_time , total_response_time = 0 ,0
    while len(hq) > 0:
        dur ,arr = heapq.heappop(hq)
        print('cr+ dr' , current_time+ dur , 'ar + dr' ,arr +dur)
        current_time = max(current_time + dur, arr+dur)
        total_response_time += current_time -arr
    
        print('dur' ,dur , 'arr' , arr  , 'current_time' , current_time ,'total_response_time' , total_response_time)
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            print('is remained' , tasks[0][1] , current_time)
            heapq.heappush(hq, tasks.popleft())
        if len(tasks) > 0 and len(hq) == 0:
            heapq.heappush(hq, tasks.popleft())
    return total_response_time // len(jobs)
jobs = [[0, 3], [4, 3], [10, 3]]	

t = solution(jobs)
print(t)