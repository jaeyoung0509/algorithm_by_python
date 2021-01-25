'''
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

5편 중 3번 이상 인용 3편 이상 나머지 논문이 3번 이하
'''

def solution(citations):
    citations.sort(reverse = True)
    print(citations)
    for i in range(len(citations)):
        if(len(citations) ==1):
            if(citations[i] == 0):
                return 0
            return 1
        if(i >= citations[i]):
            return i
        elif(i == len(citations)-1):
            return i+1
        

citations =[10, 50, 100]
#1524 999 790 540 22 10 2
print(solution(citations))
