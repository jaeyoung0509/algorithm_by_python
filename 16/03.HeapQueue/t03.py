import heapq
import re
def solution(operations):
    answer = []
    hq = []

    for i in operations:
        if "I" in i:
            t = re.sub("I","",i)
            heapq.heappush(hq, int(t))
        if "D 1" in i and len(hq) >0:
            hq.remove(hq[-1])
            
        if "D -1" in i and len(hq) >0:
            heapq.heappop(hq)
    if hq == []:
        return [0 ,0]
    return [max(hq) , min(hq)]



operations =["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
solution(operations)