'''
미로탈출
n *m 직사각형 형태의 미로  0 : 괴물  o  , 1:괴물 x 최단 거리
'''
#모든 노드의 값을 정보로 넣으면 된다..
from collections import deque
graph = [
    [1 , 0 , 1 ,0 ,1 ,0],
    [1 , 1 , 1 ,1 ,1 , 1],
    [0 , 0 , 0, 0 , 0, 1 ],
    [1 , 1 , 1, 1 , 1, 1 ],
    [1 , 1 , 1 , 1 , 1 ,1]
]
#이동할 네 방향 add
dx = [0 ,0 ,1 ,-1]
dy = [-1 , 1 , 0 , 0]
#n , m
n= len(graph)
m = len(graph[0])
def  bfs(x ,y ):
    distance= 1
    queue =deque()
    queue.append(( x,y))
    while queue:
        x ,y = queue.popleft()
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(nx >=n or nx<0 or ny >=m  or ny < 0):
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx ,ny))
    return graph[n-1][m-1]


print(bfs(0 ,0))


