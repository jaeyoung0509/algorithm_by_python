data = [-15 , -6 , 1, 3, 7]
def s(data):
    for i in range(len(data)):
        if data[i] == i:
            return i
    return -1


print(s(data))

