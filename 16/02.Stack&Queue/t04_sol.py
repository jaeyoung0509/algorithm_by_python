from collections import deque
def solution(priorities , location):
    dq = deque([(i ,v) for v , i in enumerate(priorities)])
    answer = 0
    while(len(dq)):
        pop = dq.popleft()
        if dq and max(dq)[0] > pop[0]:
            dq.append(pop)
        else:
            answer += 1
            if (pop[1] == location):
                break
    return answer



priorites = [1, 1, 9, 1, 1, 1]
location = 0
t = solution(priorites , location)
print(t)