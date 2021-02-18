# 두 자연수 p와 q를 입력받아 최소공배수를 구하는 알고리즘을 단계별로 나누어 자세히 설명하기
# (힌트: 유클리드호제법 및 최대공약수와 최소공배수의 관계 활용)

def gcd(a, b):
    while b != 0:
        a = a % b
        a, b = b, a
    return a

a = int(input("첫 번재 숫자"))
b = int(input('두 번재 숫자'))

print('최대공약수',  gcd(a, b))

print('최소공배수', a*b/gcd(a, b))



