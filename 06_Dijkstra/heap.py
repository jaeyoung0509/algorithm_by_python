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
import heapq
def heapq(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h ,value)