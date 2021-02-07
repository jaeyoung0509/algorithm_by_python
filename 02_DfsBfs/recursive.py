#recursive function = 재귀함수 = 자기 자신을 다시 호출하는 함수
def recursive_function(i):
    if i == 100:
        return
    print(i , '번째 재귀함수에서 ' ,i+1 , '번째 재귀함수를 호출 합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀함수를 종료합니다.')
#파이선에선 재귀함수 재귀함수 depth가 정해져있음.
recursive_function(1)

#컴퓨터 내에선 스택 자료구조로 메모리로 올라감
#재귀함수 종료 조건 명시해야댐
#100번째 재귀함수까지 호출한 후 재귀함수를 종료 -> stack frame 