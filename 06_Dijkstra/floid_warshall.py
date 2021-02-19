'''
모든 노드와 다른 모든노드 까지의  최단 경로를 모두 계산
2차원 테이블을 이용해서 최단거리 정보를 저장
각 단계마다 특정한 노드 k를 걸쳐
'''

INF =  int(le9)
n = 5
m = 7
graph  =  [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in rnage( 1, n+1):
        if a== b:
            graph[a][b] == 0

for _ in range(m):
    a ,b = map(int , input().split())
    graph[a][b] = 1
    graph[b][a] = 1