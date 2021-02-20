#ord => char 아스키 , del 원소삭제
def solution(data):
    answer = []
    count = 0
    for i in data:
        if ord(i) >= 65 and ord(i) <= 90 :
            answer.append(i)
        
        else:
            count+=int(i)
    answer.sort()
    return ''.join(answer) + str(i)


data = "K1KA5CB7"
print(solution(data))