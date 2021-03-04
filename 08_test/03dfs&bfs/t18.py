def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count +=1
        else:
            count -=1
        if count == 0:
            return i
#올바른 문자열인 지 확인
def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False  #쌍이 맞지 않는 경우엔 False 반환
            count -=1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    print(index)
    u = p[:index+1]
    v = p[index +1 :]
    print('u', u , 'v' ,v)
    # 올바른 괄호 문자열이라면  v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        answer = u +solution(v)
    else:
        print(" u is not  right words")
        answer= '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) #첫번째 문자와 마지막 문자를 제거
        print("zzzzz" ,u , answer)
        for i in range(len(u)):
            print("Z")
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer

print(solution("()))((()"))