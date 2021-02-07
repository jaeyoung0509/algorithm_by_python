'''
최단경로가 5000개 이하라면 기존 알고리즘으로 구현 가능 하지만
10,000개이상은 nop
priority queue(우선순위 큐):우선순위가 가장 높은 데이터를 먼저 삭제하는 자료구조
cf)
stack : 가장 나중에 삽입
queue : 가장 먼저 삽입
prioirty queue : 가장 우선순위가 높은 데이터
->heap을 이용해 (내부적으로 트리구조)
최소 heap ,최대 heap
'''
#heap은 삽입 삭제 logn이 걸림
import heapq
#파이선은 minheap으로 
def heapsort(iterable):
    h = []
    result = []
    #모든 원소를 heap 에 삽입
    for value in iterable:
        heapq.heappush(h , value)
        #최대힙을 구현을 원하는 경우 (h , -value)
    #힙에 삽입된 모든 원소를 꺼내어 담기
    for i in range (len(h)):
        result.append(heapq.heappop(h))
        #최대힙을 구현을 원하는 경우 (-heapq.heappop(h))
    return result

result = heapsort( [ 1,3 5, 6, 7 8, ,2 ,5])
print(result)