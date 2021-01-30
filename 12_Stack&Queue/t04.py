'''
일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄합니다. 그렇기 때문에 중요한 문서가 나중에 인쇄될 수 있습니다. 이런 문제를 보완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다. 이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.

'''
from collections import deque
def solution(priorities , location):
    dq = deque([(i ,v) for v , i in enumerate(priorities)])
    answer = 0
    print(dq)
    while(len(dq)):
        pop = dq.popleft()
        if dq and max(dq)[0] > pop[0]:
            dq.append(pop)
        else:
            answer += 1
            if (pop[1] == location):
                break
    return answer

priorities = [1, 1, 9, 1, 1, 1]
location = 0
solution(priorities , location)