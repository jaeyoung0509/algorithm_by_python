'''
n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.


'''
def solution( numbers ,target):
    n = len(numbers)
    answer = 0
    def dfs(idx ,result):
        if idx ==n:
            if result == target: