def sol(data , n):
    tmp = -1
    t = ()
    for i in range(len(data)):
        for j in range(i+1 , len(data)):
            for k in range(j+1 , len(data)):
                s  = data[i] + data[j] + data[k]
                if( s > tmp and s <= n):
                    tmp = s
                    t = (data[i] , data[j] ,data[k])
    return t


data = [5, 6, 7, 8, 9]
print(sol(data , 21))