def sol(data):
    count = 1
    stack = []
    result = []
    for i in range(len(data)):
        while count <= data[i]:
            stack.append(count)
            count += 1
            result.append('+')
        if stack[-1] == data[i]:
            stack.pop()
            result.append('-')

        else:
            return 'no'
    return result





data = [ 4 , 3, 6 , 8 , 7, 5, 2, 1]

print(sol(data))