'''
n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.


'''

from collections import deque
def solution( numbers , target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0] ,0 ])
    queue.append([-1 * numbers[0] , 0])
    while queue:
        temp ,idx = queue.popleft()
        print (temp , numbers[idx])
        idx += 1
        if idx < n:
            #print("www" , idx , temp , numbers[idx])
            queue.append([temp + numbers[idx] , idx])
            queue.append([temp - numbers[idx] ,idx])
        else:
            if temp == target:
                answer += 1
    return answer 

print(solution([1, 1, 1, 1, 1 ] , 3))