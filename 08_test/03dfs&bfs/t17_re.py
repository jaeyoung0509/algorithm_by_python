from collections import deque

n, k = map(int , input().split())
dx = [-1 , 1, 0 , 0]
dy = [0 , 0 , -1 ,1]
graph ,data = [] , []

for i in range(n):
    graph.append(list(map(int , input().split())))
    for j in range(k):
        if graph[i][j] != 0 :
            data.append((graph[i][j] , 0 , i , j))

data.sort()
queue = deque(data)
target_s ,target_x , target_y = map(int , input().split())
print(queue)
while queue:
    virus ,s , x ,y =  queue.popleft()
    if s == target_s:
        print(graph[target_x-1][target_y -1])
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx and nx < n and 0 <= ny and ny <k:
            if graph[nx][ny] == 0:
                print('virus' , virus , 'grpah', nx ,ny)
                graph[nx][ny] = virus
                queue.append((virus, s+1, nx, ny))

