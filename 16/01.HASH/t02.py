'''
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
'''


def solution(phone_book):
    phone_book.sort()
    a = phone_book[0]
    for i in range(1, len(phone_book)):
        if a in phone_book[i]:
            return False
    return True



phone_book = ["119", "97674223", "1195524421"]
solution(phone_book)