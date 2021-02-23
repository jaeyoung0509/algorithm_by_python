import hashlib
def sol(data):

    return hashlib.sha256(data.encode())


data ='Backjoon'

print(sol(data))