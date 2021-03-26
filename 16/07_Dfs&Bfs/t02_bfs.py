from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    q = deque()
    for k in range(n):
        if visited[k] == False:
            q.append(k)
            while q:
                com = q.popleft()
                visited[com] = True
                for i in range(n):
                    if i != com and computers[com][i] == 1:
                        if visited[i] == False:
                            answer
                            q.append(i)
            answer += 1
    return answer



n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
s = solution( n, computers)
