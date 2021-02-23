'''
네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.
풀이 : 컴퓨터가 연결되어잇는 경우 1 , 총 몇개의 네트워크의 갯수 
bfs ? dfs? ........적기
'''
from collections import deque
def dfs(computers , visited , u):
    queue = deque([0])
    while queue:
        pop = queue.popleft()
        if visited[pop] == 0:
            visited[pop] = 1
        for i in range(0 , len(computers)):
            if computers[pop][i] == 1 and visited[i] == 0:
                queue.append(i)

def solution(n, computers):
    answer = 0
    visited = [0] * 
    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	