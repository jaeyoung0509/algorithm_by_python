def soulution(card):
    answer = -1
    for i in card:
        if  min(i) > answer:
            answer = min(i)
    return(answer)


card =  [ [ 3, 1, 2] , [ 4, 1, 1] , [2 , 2,2]]
t = soulution(card)
print(t)