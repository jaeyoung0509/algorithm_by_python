a = [ 1 ,2, 5 ,4 ,3]
b = [5, 5, 6 , 5, 5]
a.sort(reverse= True)
b.sort()
for i in range(len(a)):
    if a[i] <  b[i]:
        a[i] = b[i]
    else:
        break
print(sum(a))