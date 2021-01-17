'''
bfs = Breadth-First-Search
bfs 는 너비 우선 탐색이라고도 부르며 , 그래프에서 가장 가까운 노드부터 우선적으로 탐색하는 알고리즘
큐를 사용하며
1.탐색노드에서 큐에 삽입하고 방문처리 
2.큐에서 노드를 꺼낸 뒤 해당 노드의 인접노드에서 방문하지않은 노드 처리
'''

from collections import deque
def bfs(graph , start , visited):
    queue = deque([start])
    print(queue)
    visited[start] =True
    #queue 가 빌 때 까지 반복
    while queue:
        #queue에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print ( v, end = '\t')
        #아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
graph=[
[],#0 x
[2,3,8], #1
[1,7],#2
[1,4,5],#3
[3,5],#4
[3,4],#5
[7],#6
[2,6,8],#7
[1,7]#8
]
visited=[False] * len(graph)
bfs(graph , 1 , visited)