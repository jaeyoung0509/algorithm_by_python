'''
음료수 얼려 먹기
n * m 크기의 얼음 틀이 있다. 구멍이 뚤려 잇는 부분은 0 ,칸막이 존재 1
'''
graph = [
    [0 , 0 , 1, 1, 0],
    [0 , 0 ,0 , 1, 1], 
    [1 , 1 ,1 , 1 , 1],
    [0 , 0, 0, 0 , 0, 0]
    ]
n , m = len(graph) , len(graph[0])
def dfs(x ,y):
    if x >=n or x<0 or y >=m or y <0:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        bfs(x+1 ,y)
        bfs(x-1 ,y)
        bfs(x , y+1)
        bfs(x , y-1)
        return True
    return False

    