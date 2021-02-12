def soulution(n ,directions)
    dy= [ -1, 1, 0,0]
    dx =[ 0, 0, 1 -1,]
    move_types = ['L' , 'R' , 'U' , 'D']

    for direction in directions:
        for i in range(len(move_types)):
            if move_types[i] == direction:
                nx = x + dx[i]
                ny = y + dy[i]
            if nx <1 or ny <1 or nx > n or ny >n :
                continue
        x ,y = nx ,ny
    return answer


n = 5
directions=['R' , 'R' , 'R' , 'U' ,'D' ,'D']
soulution(n , directions)