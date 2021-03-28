def soulution(n):
    steps = [(-2 , -1) , (-2 , 1) , (-1 ,-2) , (-1 , 2) , (1, -2) , (1, 2) , (2 ,-1 ) , (2, 1)]
    row = int(n[1])
    column = int(ord(n[0]))- int(ord('a')) + 1
    answer = 0c
    print(column)
    for step in steps:
        next_row += step[0]
        next_col += step[1]
        if next_row >= 1 and next_row <=8 and next_col >=1 and next_row <=8:
            answer+=1
    return answer


n = 'a8'
soulution(n )