def solution(participant ,completion):
    data = dict()
    for i in participant:
        if i not in data:
            data[i] =0
        else:
            asd = i
            data.update[i ,data[i] + 1]
    for i in completion:
        if i in data:
            data.update[i , data[i] +1]
    for i in data:
        print(data)

participant =["marina", "josipa", "nikola", "vinko", "filipa"]
completion =["josipa", "filipa", "marina", "nikola"]
a = solution(participant ,completion)
print(a)