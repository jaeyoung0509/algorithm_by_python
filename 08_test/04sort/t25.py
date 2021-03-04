import heapq

data = [10 ,20, 40]
queue = []
result = 0
for i in data:
    heapq.heappush(queue , i)


while(len(queue) != 1):
    one_ = heapq.heappop(queue)
    two_ = heapq.heappop(queue)
    result += one_+two_
    heapq.heappush(queue ,one_ + two_)

print(result)