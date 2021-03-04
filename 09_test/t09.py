
def sol(data):
    
    return sorted(sorted(data , key = lambda x : x[0]) , key = lambda x : x[1])

data = []
data.append((  3, 4, ))
data.append((1 ,1 ))
data.append((1, -1 ))
data.append((2, 2))
data.append((3, 3))


print(sol(data))