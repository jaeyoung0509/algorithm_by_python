def fibo(x):
    if x ==1 or x ==2 :
        return 1
    return fibo(x-1) + fibo(x-2)
'''
여기서 문제점 -> 중복되는 점이 많아 시간이 기하 급수적으로 증가 
-> dynmaic programing을 통해 해결해 보잔
1.최적 부분 구조 : 큰 - > 작은
2.중복되는 부분 문제 : f3: f2 + f1 / f4: f3+ f2  이런식으로 f2가 중복중복
-> 해결방법 상향식 : Memoization (탑다운)
메모리공간에 메모 하는 기법 : 같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져옵니다 , 값을 기록해 놓는다는 점에서 캐싱 이라고도 함ㄴ
->보텀업 (상향식): 결과 저장용 리스트는 dp 테이블이라고 도 부름
엄밀히 말해 메모제이션은 이전 계산된 결과를 일시적으로  기록
'''
def fibo_TopDownMemozation(x):
    d = [0] * 100
    if x ==1  or x == 2 :
        return 1
    #이미 계산한적이 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]

    d[x] = fibo(x-1 ) + fibo(x-2)
    return d[x]

def fibo_BottomUp(x):
    d = [0] * 100
    d[1] = 1
    d[2] = 1
    for i in range (3, x+1):
        d[i] = d[i-1 ] + d[i-2]
    return d[x]

print(fibo_TopDownMemozation(4))

