'''
특정 조건이 부합할 때만 사용가능 -> 이땐 매우 빠름 
몇번 나왔는지 확인해서 
'''
array = [ 7,  5 , 9 ,0 , 3 , 1 ,6 ,2 ,4 ,8 , 8, 8]
count = [0] * (max(array) + 1 )
for i in range(len(array)):
    count[array[i]] += 1

for i in range (len(count)):
    for j in range(count[i]):
        print( i , end = '')