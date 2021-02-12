'''
bfs = Breadth-First-Search
bfs 는 너비 우선 탐색이라고도 부르며 , 그래프에서 가장 가까운 노드부터 우선적으로 탐색하는 알고리즘
큐를 사용하며
1.탐색노드에서 큐에 삽입하고 방문처리 
2.큐에서 노드를 꺼낸 뒤 해당 노드의 인접노드에서 방문하지않은 노드 처리
'''
#breadth first search
from collections import deque
def bfs(graph , start, visited):
    queue = deque([start]) #start 를 시작으로 list -> queue 로 만들기 위해
    visited[start] = True
    while queue:
        v = queue.popleft()
        print ( v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
graph = [
    [],
    [2 , 3, 5] , 
    [1 ,7 ], 
    [1 , 4, 5] ,
    [3, 5],
    [3, 4],
    [7] ,
    [2 , 6, 8] ,
    [1 , 7]
]
visited = [False] * 9
bfs(graph , 1 , visited)