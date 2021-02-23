from collections import deque
def bfs(graph ,start_node):
    visited = []
    need_visit = deque([start_node]) 
    while need_visit:
        node = need_visit.popleft()
        #pop(0)
        if node not in visited:
            visited.append(node)
            #extend : 붙이다 
            need_visit.extend(graph[node])
    return visited

graph = dict()
graph['A'] = ['B' ,'C']
graph['B'] = ['A' ,'D']
graph['C'] = ['A']
graph['D'] = ['B']
a =  bfs(graph,'A')
print(a)