'''
스택 : 선입 후출 자료 구조 
입구와 출구가 동일한 형태 (박스 쌓기)
파이선에선 list를 이용해서 
append ,pop  , [::-1]
'''
'''
큐 : 먼저 들어온 데이터가 나가는 선입선출
큐는 입구와 출구가 모두 뚤려 있는 터널 형태
from collections import deque

queue = deque()
queue.append()
queue.popleft -> 빼기
queue.revers()
'''

'''
재귀함수 란 자기 자신을 다시 호출 하는 함수
재귀함수 종료 조건 반드시 명시
'''

#df는 깊이 우선탐색
def dfs(graph , v , visited):
    #현재 노드를 방문처리
    visited[v] = True
    print(v , end = '')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph , i , visited)

graph = [
    [],
    [2,3,8],
    [1, 7] ,
    [1, 4, 5] ,
    [3, 5], 
    [7] ,
    [2 , 6, 8] ,
    [1 ,7]
]
#각 노드가 방문된 정보를 표현
visited = [False] * 9
#정의된 dfs 함수 호출
dfs(graph , 1 ,visited)