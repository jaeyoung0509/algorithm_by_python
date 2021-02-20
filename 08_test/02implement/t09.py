def solution(data):
    answer=  len(data)
    #1개 단위 step으로 압축 단위를 늘려가며 확인
    for step in range(1 , len(data) //2 + 1):
        compressed = ""
        prev = data[0:step]
        print('prev', prev)
        count = 1
        #단위(step)크기만큼 증가하며 이전 문자열과 비교
        for j in range(step , len(data) ,step):
            if prev == data[j: j+ step]:
                print("step" , j)
                print("data" , data[j : j + step])
                count += 1
            #다른 문자열이 나왔다면
            else:
                compressed += str(count) + prev if count>= 2 else prev
                prev = data[j: j+ step]
                print("not" , data[ j : j + step] , compressed)
                count = 1
        #남아있는 문자열에 대해 처리
        compressed += str(count) + prev if count >= 2 else prev
        print(compressed)
        answer = min(answer ,len(compressed))
    return answer



data = "abcdabcd"
print(solution(data))