from collections import deque
def solution(number, k):
    q = deque([number[0]])
    for i in number[1:]:
        while q and  i > q[-1] and  k >0:
            k -=1
            q.popleft()
        q.append(i)
    if k != 0:
        q = q[:-k]

    



number= "0101"
k = 2
a = solution(number, k)
print(a)