import collections
#데이터의 개수를 셀 때 유용한 collections 모듈 의 counter
def solution(participant ,completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(collections.Counter(participant))
    return answer



a= ["aa" , "bb"]
b = ["bb"]
c = solution(a,b)
print(list(c.keys()))