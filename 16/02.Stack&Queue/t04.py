from collections import deque
#파이선 max 함수 쓸때 tuple로 이루워진경우 0번쨰 인덱스만 참조 가능..?
def solution(priorities, location):
    list_ = []
    q = deque([(idx , val) for val, idx in enumerate((priorities))])
    for idx ,val in enumerate(priorites):
        list_.append((val ,idx))
    count =  0
    q = deque(list_)
    print(max(q))
    while (q):
        tmp = q.popleft()
        if  max(q)[0] > tmp[0]:
            q.append(tmp)
        else:
            count += 1 
            if (tmp[1] == location):
                break

    return count
priorites = [1, 1, 9, 1, 1, 1]
location = 0
t = solution(priorites , location)
print(t)