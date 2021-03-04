#모든 간선 비용이 1이다 ->bfs 를 이용해서 문제 해결
from collections import deque
#도시의 갯수 n , 도로의 갯수 m , 거리 정보 k , 출발 도시의 번호 x
n , m , k ,x =4 , 4, 2, 1
graph = [ [] for _ in range( n+1)]
graph[1].append(2)
graph[1].append(3)
graph[2].append(3)
graph[2].append(4)

distance = [-1] * (n+1)
distance[x] = 0 #출발 도시까지의 거리는 0 으로

q =deque([x])
while q:
    now = q.popleft()
    print(now)
    for next_node in graph[now]:
        print('next_node' , next_node , 'distance[next_node]' , distance[next_node])
        if distance[next_node] == -1:
            distance[next_node] = distance[now] +1
            print(distance[next_node])
            q.append(next_node)

check = False
for i in range(1 , n+1):
    if distance[i] == k :
        print(i)
        check = True


if check == False:
    print(-1)
 