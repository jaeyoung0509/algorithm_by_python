'''
dfs 란 depth first search 깊이 우선탐색 이라 부르면 스택(재귀함수)를 활용하여 깊은 부분을 우선적으로 탐색
1.탐색 시작 노드를 스택에 삽입 방문처리
2.스택의 최 상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리 방문하지 않은 인접 노드가 없으면 
스택에서 최상단 노드를 꺼냄
3.더이상 2번의 과정을 수행 할 수 없을때 까지 실행
[방문 기준]: 번호가 낮은 노드부터 방문 가정
'''
#dfs_recursive (graph , node , visisted) ->1 방문처리 , 2.for문을 통해 해당 노드와 연결된 노드(낮은순)재귀로 반복
#여기서 스택을 쓰지않고 만들 수 있던 이유 : 재귀로 반복하기 때문에 -> 재귀는 스택의 구조를 가지고 잇음

def dfs(graph , v , visited):
    #현재 노드를 방문처리
    visited[v] = True
    print('v : ' ,v  , 'visited[v] : ' , visited[v])
    for i in graph[v]:
        if not visited[i]:
            dfs(graph , i , visited)
    return visited

graph = [
    [],
    [2, 3, 8],
    [1 ,7 ], 
    [1 , 4, 5],
    [3, 5 ],
    [3, 4] ,
    [7], 
    [2 ,6 ,8], 
    [ 1, 7]
]
visited= [False] * 9

a = dfs(graph , 1 ,visited)
print(a)