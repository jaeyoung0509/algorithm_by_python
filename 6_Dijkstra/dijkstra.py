'''
Dijkstra(다익스트라, 최단경로) 알고리즘 : 가장 짧은 경로를 찾는 알고리즘
다양한 문제상황
-한지점에서 다른 지점
-한지점에서 모든 지점
-모든지점에서 다른 지점
각 지점은 그래프에서 노드 , 지점 에서 연결된 그래프는 간선  
다익스트라 알고리즘은 음의 간선이 없을 때 정상적으로 표현
'''
'''
출발 노드를 설정
최단 거리 테이블을 초기화
방문하지 않은 노드중에서 가장 짧은 노드를 선택
해당 노드를 걸쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
'''

import sys
input sys.stdin.readline
INF = int(le9) #무한 값

n, m = map(int , input().split())
start  = int (input())

#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [ [] for i in range( n +1)]
visited = [False] * (n+1)
#최단 거리 테이블을 모두 무한으로 초기화
distance  = [INF] * (n+1)

#모든 간선 정보를 입력받기
for _in range(m):
    a, b, c = map(int , input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,c))

#방문하지 않은 노드 중에서 , 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index =  0
    for i in range(1 ,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
        return index

def dijkstra(strat):
    #시작 노드에 대해 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]