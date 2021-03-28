n = int(input())
k = list(map(int , input().split()))
idx = 0
result  = 1
k.sort(reverse=True)
idx += k[0]

while  idx < n:
    idx += k[idx]
    result += 1 
print(result)
