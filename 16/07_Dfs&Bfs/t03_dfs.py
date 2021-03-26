answer = 0
def solution(begin, target, words):
    global answer
    if target not in words:
        return 0
    visited = [0] * len(words)  

    answer= dfs(begin , target , words , visited)
    return answer

def dfs(begin , target , words , visited):
    global answer
    q = [begin]
    while q:
        queue = q.pop()
        if queue == target:
            return answer
        for w in range(len(words)):
            temp_wrod = words[w]
            if sum([x!=y for x,y in zip(temp_wrod, queue)]) ==1 :
                if visited[w] !=0 :
                    continue
                visited[w] = 1
                q.append(temp_wrod)
        print(q)
        answer += 1
    
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
solution(begin , target , words)