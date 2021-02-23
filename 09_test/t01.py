def sol(data):
    tmp0 = sorted(data)
    tmp1 = sorted(data , reverse= True)
    print( tmp0 , tmp1 , data)
    for i in range(len(data)):
        if data[i] == tmp0[i]:
            if i == len(data)-1:
                return "ascending"
        
        elif data[i] == tmp1[i]:
            if i == len(data) -1:
                return "decending"

        else:
                return "mixed"


data = [5 , 9, 2, 1]

print(sol(data))