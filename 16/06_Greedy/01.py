def solution(n, lost, reserve):
    #중복을 제거 하기 set
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    print('reserve' ,set_reserve , 'set_lost' ,set_lost)
    for i in set_reserve:
        if i-1 in set_lost: #무슨 의미?
            print( 'i' , i ,'i-1', i-1)
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            print( 'zzzi' , i ,'i-1', i-1)
            set_lost.remove(i+1)
    return n-len(set_lost)
n = 5
lost = [1, 3, 5] #2 
reserve = [2, 3, 6] #3
solution(n, lost, reserve)

