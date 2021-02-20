def rotate_a_matrix_by_90_degree(a):
    n = len(a) #행 길이
    m = len(a[0]) # 열 길이
    result= [[0] * for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
        return result

#자물쇠 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length =


def solution(data):
    answer = 0
    return answer


key = [ [ 0 , 0 ,0] , [1 , 0 , 0] , [0 , 1, 1,]]
lock = [ [ 1, ,1 ,1 ] , [1 , 1, 0] , [1, ,0 , 1]]
