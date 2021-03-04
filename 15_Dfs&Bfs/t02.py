from collections import deque
def solution(n, computers):
    answer = 0
    visited = [0] * len(n)
    queue = deque(visited.index(0))
    while queue:
        node = queue.popleft()
        visited[node] = 1
        for i in range(len(n)):
            if visited[i] == 0 and  computers[node][i] == 1:
                print(i , computers[node][i])
                queue.append(i)
    answer += 1
  return answer


solution(computers, 0)