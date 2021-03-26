from collections import deque
glboal answer
def solution(begin , target ,words):
    if target not in words:
        return 0
    visited = [0 for i  in words]
    answer = dfs(begin ,target ,words ,visited)
    return answer
def dfs(begin , target ,words , visited):
    global answer
    q = queue()
    q.append(target)
    while q:
        word = q.popleft()



begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]