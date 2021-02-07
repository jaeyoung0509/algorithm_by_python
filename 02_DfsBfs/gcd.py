#유클리드 호제법을 재귀를 통해
#두 자연수 (A>B) a를 b로 나눈 나머지를 r
#이 때 b와 r의 최대 공약수와 같다.
'''
gcd(24 ,15)
gcd(  15  , 9)
gcd(9 . 6)
gcd(6 , 3)
gcd(3 , 0)
'''
def gcd(a , b):
    if(a % b == 0):
        return a
    return gcd(b , a%b)
print(gcd(65, 15))