#enumerate ->열거하다 tuple ,list ,string 을 인자로 받아서 index, value
#dictionary 에 list를 넣어 키값 중복 피하기
#append vs extend 차이
#y= [a,b] , x.append(y)=[[a,b]]  x.extend(y) =[a,b]
#sort key : lambda x: x[1] , reverse =True
def solution( genres , plays):
    answer = []
    genres_dict = {}
    genres_list = []
    for i in range(len(genres)):
        if genres[i] not in genres_dict:
            genres_dict[genres[i]] = []
        genres_dict[genres[i]].append([i , plays[i]])
    for i in genres_dict.keys():
        temp = 0
        genres_dict[i].sort(key=lambda x: x[1], reverse=True)
        for _,play in genres_dict[i][:2]:
           temp += play
        genres_list.append([i,temp])
    genres_list.sort(key= lambda x :x[1] , reverse= True)
    for x, _ in genres_list:
        for c,d in genres_dict[x][:2]:
            answer.append(c)
    print(answer)
    return "answer"




genres = ["classic", "pop","classic", "classic", "pop"]
plays = [5100 , 600 ,150 , 800 ,2500]
solution(genres,plays)