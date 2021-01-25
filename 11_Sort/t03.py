'''
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

5편 중 3번 이상 인용 3편 이상 나머지 논문이 3번 이하
'''

def solution(citations):
    citations.sort(reverse = True)
    answer = int(0)
    for i in range(int(sum(citations,0.0)/len(citations)) , citations[0]):
        #mean ~ max
        h_up = 0
        h_down = 0
        for j in citations:
            if(j >= i):
                h_up += 1
            elif (j < i):
                h_down += 1
            if h_up > h_down and h_up >= answer:
                answer = h_up
    print(answer)
    return answer

citations =	[1524 , 2 , 999 , 790 , 540,  10 , 22]
# 
#1524 999 790 540 22 10 2
solution(citations)
