'''
n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.
'''
from collections import deque
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    q= deque()
    q.append([numbers[0] , 0])
    q.append([-1 * numbers[0] , 0])
    while q:
        val , idx = q.popleft()
        idx += 1
        if idx < n :
            q.append([val+ numbers[idx] , idx])
            q.append([val-numbers[idx] , idx])
        else:
            if val == target:
                answer += 1
                print(idx , val , answer)
    return answer



numbers	= [1, 1, 1, 1, 1]
target = 3
solution(numbers , target)