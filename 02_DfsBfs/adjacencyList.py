#인접 리스트로 표현하는 그래프 방식
graph = [ [] for _ in range(3)]

graph[0].append((1,7))
graph[0].append((2,5))
graph[1].append((0,7))
graph[2].append((0,5))
print(graph)