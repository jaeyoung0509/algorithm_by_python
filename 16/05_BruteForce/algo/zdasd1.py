def solution(s, n):
    list_ = []
    for i in s:
        list_.append(ord(i))
    answer = ''
    for i in list_:
        if int(i) == 32:
            answr+=i
        if int(i) == 122 or int(i) == 90:
            i = chr(i-25)
        answer += str(chr(i+n))
    print(answer)
    return answer


s= "z"
n = 1
solution(s, n)