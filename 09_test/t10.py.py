
def sol(data , key):
    count = 0
    for i in range(0 , len(data) , len(key)):
        if data[i:i+len(key)] == key:
            count += 1
    return count

print(sol ( "ababababa" , "aba"))