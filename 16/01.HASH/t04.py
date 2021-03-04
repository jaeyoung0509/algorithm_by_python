'''

스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다
'''


def solution(genres, plays):
    dict_ = dict()
    who_ = dict()
    answer = []
    for i in range(len(genres)):
        if genres[i] not in dict_:
            dict_[genres[i]] = [[i , plays[i]]]
            who_[genres[i]] = 0 + plays[i]
        else:
            who_[genres[i]] = who_[genres[i]] + plays[i]
            dict_[genres[i]].append([i , plays[i] ])

    lists_ = who_.keys()
    data_ = []
    for i in who_:
        data_.append((who_[i] , i))
    data_.sort(key= lambda x :x[0] , reverse= True)

    for i in data_:
        dict_[i[1]].sort( key = lambda x  : x[1] ,reverse= True)
        for j in dict_[i[1]][:2]:
            answer.append(j[0])
        #answer.append(data_[i[1]][:2])
    print(answer)
    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays  = [500, 600, 150, 800, 2500]

solution(genres , plays)