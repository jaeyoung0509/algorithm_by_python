from collections import deque

n , k = map(int , input().split())

graph = [] #전체 보드 정보를 
data = [] #바이러스에 대한 정보

for i in range(n):
    graph.append(list(map(int , input().split())))
    for j in range(n):
        if graph[i][j] != 0: #해당 위치에 바이러스가 존재하는 경우
            data.append((graph[i][j] , 0, i, j)) #바이러스 종류 시간 위치 x , 위치 y 삽입

data.sort()
print(data)
q = deque(data)

target_s , target_x , target_y = map(int , input().split())


dx = [-1 ,1 , 0 , 0]
dy = [ 0, 0, -1 ,1]

while q:
    virus ,s, x ,y = q.popleft()
    if s== target_s:
        print(graph[target_x-1][target_y-1])
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx and nx < n and 0<= ny and ny <n:
            #아직 방문하지 않은 위치라면 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                print('virus' , virus , 'grpah', nx ,ny)
                q.append((virus ,s+1 , nx ,ny))

