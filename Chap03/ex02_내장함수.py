# 파이썬 내장 함수는 외부 모듈과 달리 import가 필요없다.

# type(object) => 자료형을 알려줌.
print(type("abcd"))     # <class 'str'>
print(type([]))         # <class 'list'>

# id(object) => 객체의 주소 값 반환
a = 3
print(id(a))    # 1893312464
print(type(a))  # <class 'int'>

# pow(x, y) => x를 y만큼 제곱한 결과 반환
print(pow(3, 4), pow(2, 3)) # 81 8

# sum(iterable) => 합계 반환
print(sum((1,2,3,4,5)), sum([1,2,3]))   # 15 6

# max(열거형 자료), min(열거형 자료)
print(max([1,2,3]), max('python'))  # 3, y
print(min([1,2,3]), min('python'))  # 1, h

# round(number) => 반올림 수 반환
print(round(4.6))   # 5
print(round(4.1))   # 4
print(round(3.141592, 3))   # 3.142

# eval(계산 가능한 문자열) => 문자열을 계산한 결과값 반환
print(eval('1+2'))  # 3

# list(열거형 자료) => 리스트 반환
print(list('python'))   # ['p', 'y', 't', 'h', 'o', 'n']
print(list((1,2,3)))    # [1, 2, 3]

# enumerate() => 열거형 자료형을 입력 받아 인덱스 값과 자료를 반환
for i, char in enumerate('python'):
    print(i, char)

# filter(함수f, 열거형 자료) => 열거형 자료가 주어진 함수에서 실행되었때 참인 값만 반환
def positive(n):
    return n>0

print(list(filter(positive, [-1, 3, 2, 0, -7, 9])))         # [3, 2, 9]
print(list(filter(lambda n: n>0, [-1, 3, 2, 0, -7, 9])))    # [3, 2, 9]

# map(함수f, 열거형 자료) => 함수f가 수행한 결과를 반환
def two_times(x):
    return x*2

print(list(map(two_times, [1,2,3,4])))      # [2, 4, 6, 8]
print(list(map(lambda x: x*2, [1,2,3,4])))      # [2, 4, 6, 8]

# range([start], stop, [step]) => 입력받은 숫자에서 반복 가능한 객체 반환
print(list(range(5)))           # [0, 1, 2, 3, 4]
print(list(range(1, 5)))        # [1, 2, 3, 4]
print(list(range(1, 10, 2)))    # [1, 3, 5, 7, 9]

# sorted(열거형 자료)
print(sorted([3, 1, 2]))    # [1, 2, 3]
print(sorted('zero'))       # ['e', 'o', 'r', 'z']

