#스코빌 점수
import heapq
def solution(scoville, k):
    answer = 0
    hq = scoville
    heapq.heapify(hq)
    if hq[0] >= k:
        return 0
    while hq[0] < k :
        if len(hq) > 1:
            item1 = heapq.heappop(hq)
            answer +=1 
            item2 = heapq.heappop(hq)
            heapq.heappush(hq ,( item1 + item2 *2))
        else:
            return -1
    return answer


scoville = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(scoville, k))