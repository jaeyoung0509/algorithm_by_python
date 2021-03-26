answer = 0 
def dfs(begin ,target ,words, visited):
    global answer #global 전역변수
    stack = [begin]
    while stack:
        stack = stack.pop()

        if stack == target:
            return answer
        for j in range(len(words)):
            if len([ i for i in range(len(words[j])) if words[i][j] != stack[j]]) == 1:
                if visited[i] != 0:
                    continue
                visited[i] = 1
                stack.append(words[i])
        answer +=1
    return answer

def solution(begin , target ,words):
    if target not in words:
        return 0
    visited = [0 for i  in words]
    answer = dfs(begin ,target ,wrods ,visited)