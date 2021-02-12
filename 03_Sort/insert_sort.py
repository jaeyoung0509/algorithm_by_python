'''
insert_sort 는 거의 정렬이 되어 있을 떄 빠른 속도를 보여줌 
첫번째 인덱스의 원소는 정렬 되어 있다 가정하고 두번째 원소 부터 시작한다.
ex) array = [ 7 ,5 , 9 , 0 , 3, 1 ,6 , 2, 4 ,8 ]
array[0]의 값인 7은 정렬되어 있다 가정하고
array[1]의 값인 5가 어떤 위치로 들어갈지 판단한다.
들어 갈 수있는것은 ㅁ  <- 7 -> ㅁ 두군데 
최악  o(n*2)  최선 o(n)
'''


array = [ 7 ,5 , 9 , 0 , 3, 1 ,6 , 2, 4 ,8 ]

for i in range( 1 , len(array)):
    for j in range(i , 0  ,-1):
        if(array[j-1] > array[j]):
            print(array [j-1] , array[j])
            array[j-1 ]  , array[j] = array[j] , array[j-1]
        else:
            break
print(array)