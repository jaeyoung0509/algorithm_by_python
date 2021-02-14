INF = int(1e9)

n , m = 6 ,11
graph = [[] for i in range (n +1)]

visited = [False] * (n+1)
distance = [INF] * (n+1)


graph[1].append((2,2))
graph[1].append((3,5))
graph[1].append((4,1))
graph[2].append((3,3))
graph[2].append((4,2))
graph[3].append((2,3))
graph[3].append((6,5))
graph[4].append((3,3))
graph[4].append((5,1))
graph[5].append((3,1))
graph[5].append((6,2))
#가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1 , n+1):
        if distance[i] < min_value and  not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    #시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
