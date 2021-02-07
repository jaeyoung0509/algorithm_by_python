'''
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

'''
import heapq
def solution(scoville , k):
    answer = 0
    heap =[]
    for i in scoville:
        heapq.heappush(heap , i)
    while heap[0] < k:
        try:
            item = heapq.heappop(heap)
            item2 = 2 * heapq.heappop(heap)
            heapq.heappush(heap , (item+ item2))
            answer += 1
        except IndexError:
            return -1  
    return answer

scoville =[1, 2, 3, 9, 10, 12]
k = 7
solution(scoville  , k)