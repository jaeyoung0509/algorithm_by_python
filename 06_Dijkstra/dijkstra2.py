from collections import heapq

def dijkstra(graph ,start):
    distance = { node : float("int") for node in graph}
    distance[start] = 0
    queue= []
    heapq.heappush(queue , [distance[start] , start])