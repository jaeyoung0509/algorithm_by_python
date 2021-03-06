from collections import deque
def solution(prices):
    price_queue = deque(prices)
    answer = []
    while len(prices) != 0:
        price = price_queue.popleft()
        count = 0
        for i in price_queue :
            count += 1
            if price > i:
                break
        answer.append(count)
    return answer


#	return [4, 3, 1, 1, 0]	
prices = [1, 2, 3, 2, 3]
a = solution(prices)
print(a)