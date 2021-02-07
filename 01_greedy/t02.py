def soulution(m):
    money = m
    money_list = [500 , 100 ,50 , 10]
    for i in money_list:
        temp = money // i
        money = money - (temp * i)
        print(i , temp , money)
        if(money == 0):
            return


soulution(4800)
        