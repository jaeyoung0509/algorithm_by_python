#set 자료 형 사용하기

def sol(data , x): 
    data = set(data)
    if(x in data) :
        return 'true'

    else:
        return 'false'

d= sol([1 , 2, 3, 4, 5], 3)
print(d)