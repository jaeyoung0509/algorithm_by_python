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
'''
기본원리는 동일하나
-현재 가장 가까운 노드를  저장하기 위해서 힙 자료구조를 추가적으로 이용 ,
-현재 최단거리가 가장 짧은 노드를 선택해야 하므로 최소 힙을 사용    
'''
import heapq
INF = int(le9)


def dijkstra(start):
    q = []
    heapq.heappush(q (0 , start))
    distance[start] = 0
    while q:
        dist , now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph:
            cost = dist + i[1]
            if cost < distance[i][0]:
                distance[i][0] = cost
                heapq.heappush(q, (cost , i[0]))