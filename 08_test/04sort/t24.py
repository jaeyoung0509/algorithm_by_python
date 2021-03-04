data = [ 5 ,1,  7 ,9]
result = [(0 , 0)] * len(data)
for i in range(len(data)):
    sum_ = 0
    for j in range(len(data)):
        sum_ += abs(data[i] - data[j])
        result[i] = (data[i] , sum_)

result.sort(key = lambda x : (x[1] , x[0]))
print(result[0][0])