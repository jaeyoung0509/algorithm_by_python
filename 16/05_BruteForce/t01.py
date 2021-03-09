def solution(answers):
    answer = []
    answer.append([1, 2, 3, 4, 5])
    answer.append([2, 1, 2, 3, 2, 4, 2, 5])
    answer.append([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    rs = [0] * 3
    tmp = [0] * 3
    length = len(answers)
    print(length , len(answer[0]))
    if length > len(answer[0]):
        for i in range(len(answer)):
            if length > len(answer[i]):
                tmp2 = length %  len(answer[i]) 
                tmp = length // len(answer[i]) -1
                if tmp >0 :
                    answer[i] = answer[i] * (tmp +1) 
                if tmp2 > 0:
                    answer[i].extend(answer[i][0:tmp2])
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            for k in range(len(answers)):
                if j == k and  answer[i][j] == answers[k]:
                    rs[i] += 1
    tr = []
    for i in range(len(rs)):
        if rs[i] == max(rs):
            print(i )
            tr.append(i+1)
    return tr

answers= [1,3,2,4,2, 1, 2 , 1, 2, 4, 6, 7]
solution(answers)