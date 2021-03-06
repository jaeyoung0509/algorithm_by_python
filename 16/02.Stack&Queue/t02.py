def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)-1):
        for j in range(i+1 , len(prices)):
            if prices[i] <= prices[j] :
                answer[i] += 1
    
    return answer


#	return [4, 3, 1, 1, 0]	
prices = [1, 2, 3, 2, 3]
a = solution(prices)
print(a)