def sol(a):
    ascending = True
    descending = True

    for i in range(0 , len(data)-1):
        if a[i] > a[i+1]: 
            ascending = False
        elif a[i] < a[i+1]:
            descending = False
    if ascending == True:
        return 'ascending'
    elif descending == True:
        return 'descending'
    else:
        return 'mixed'


data = [5 , 3, 2, 1]

print(sol(data))