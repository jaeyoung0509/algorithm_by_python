'''
하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다. 디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다. 가장 일반적인 방법은 요청이 들어온 순서대로 처리하는 것입니다.

'''
# 해결방법->짧은 요청을 먼저수행
import heapq
def solution(jobs):
    last = -1
    now =0 
    answer = 0
    heap = []
    n = len(jobs)
    count = 0
    while (count < n):
        for job in jobs:
            if last < job[0] <= now:
                answer+=(now -job[0])
                print("zz",now  , job[0])
                heapq.heappush(heap , job[1])
            if len(heap)>0:
                print("aa",len(heap) * heap[0])
                answer += len(heap) * heap[0]
                last += now
                now += heapq.heappop(heap)
                count +=1
            else:
                now+=1
    return answer //n
jobs = [[0, 3], [1, 9], [2, 6]]
solution(jobs)