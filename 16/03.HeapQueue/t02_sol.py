import heapq
def solution(jobs):
    count , last , answer  = 0 , -1 , 0
    wait = []
    jobs.sort(key= lambda x : (x[0] , x[1]))
    #첫번째 time
    time= jobs[0][0]
    length = len(jobs)
    
    while count < length:
        for start , term in jobs:
            print('last' ,last , 'start' ,start, 'time' ,time)
            if last < start <= time:
                heapq.heappush(wait , (term , start))
        if len(wait) > 0 :
            last = time #지난 마지막 시간
            count += 1
            term , start = heapq.heappop(wait)
            time += term
            answer +=(time -start)
            print('term' ,term , 'start' ,start  , 'time' , time , 'answer' ,answer , 'last' , last)
        
        
        else:
            print('nop!' , 'last' ,last , 'start' ,start, 'time' ,time)
            time += 1
    return answer // length





jobs = [[0, 3], [4, 3], [10, 3]]	

t = solution(jobs)
print(t)