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
def bfs(x ,y):
    if x <=-1 or x>= n or y<= -1 or y>=m:
        return False
    if graph[x][y] ==0 :
        print( x, y)
        graph[x][y] =1
        bfs(x , y+1)
        bfs(x , y-1)
        bfs(x -1 ,y)
        bfs(x +1  ,y)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if bfs(i ,j ) == True:
            result+=1
print(result)