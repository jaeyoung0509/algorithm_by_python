def solution(inputs):
    answer = []
    n = inputs[0]
    count0 , count1 =  0 , 0
    if(n == 1):
        count1+=1 
    else:
        count0+=1
    for i in range( len(inputs)- 1):
        if(inputs[i] != inputs[i+1]):
            if inputs[i] == 0 :
                #i = 0 , i+1  = 1
                count0 += 1
            else:
                count1 += 1
    return(min(count0 , count1)) 
inputs = '0001100'
print(solution(inputs))