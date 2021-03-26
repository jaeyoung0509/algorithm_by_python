from collections import deque
answer = 0
def solution(n, computers):
    global answer
    visited =[False] * len(computers)
    for com in range(n):
        if visited[com] == False:
            print("*****")
            BFS(n, computers, com, visited)
            answer += 1
    return answer

def BFS(n, computers, com, visited):
    visited[com] = True
    queue = []
    global answer
    queue.append(com)
    while len(queue) != 0:
        print('Before queue' , queue , 'com' ,com , 'visited' , visited)
        com = queue.pop(0)
        visited[com] = True
        print('After queue' , queue , 'com' ,com , 'visited' , visited)

        for connect in range(n):
            # 자기자신이 아닌 경우 1 일때
            if connect != com and computers[com][connect] == 1:
                if visited[connect] == False:
                    print('True connect' , connect , 'com' , com , 'visited', visited)
                    queue.append(connect)
n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
s = solution( n, computers)
print(s)