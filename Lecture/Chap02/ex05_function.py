#region 1. 사용자 정의 함수 1
# c = 10
# def add(a, b):
#     #global c    # 전역 변수 c
#     c = a+b     # 함수 밖의 c 변수값이 바뀐다.  
#     return c

# def subtract(a, b):
#     return a-b
 
# print(add(5, 10), c)           # 15
# print(subtract(5, 10))      # -5
# print(subtract(b=5, a=10))  # 5
#endregion

#region 2. 사용자 정의 함수 2
# # 사용자에게 정수 반지름과 원주율을 입력받는 상황
# def get_input_value(msg, casting=int):
#     '''사용자에게 msg를 출력하고 입력받은 값을 casting 형태로 변환하여 반환한다.
#     이때, 사용자의 입력이 잘못된 경우 입력을 다시 요청한다.

#     Args:
#         msg(str) : input()로 출력할 문자열
#         casting(class) : 사용자에게 입력 받은 자료형

#     Return:
#         value (casting vlaue) : 사용자가 입력한 값을 캐스팅한 값
#     '''
#     while True:
#         try:
#             value = casting(input(msg))
#             return value
#         except:
#             continue

# name = get_input_value("이름을 입력하세요: ", str)
# radius = get_input_value("반지름을 입력하세요: ", int)
# pi = get_input_value("원주율을 입력하세요: ", float)
# print(name, radius, pi)
#endregion

#region 3. 입력값이 몇 개가 될지 모를 때
# # 3-1. 인자를 모두 더하는 함수
# def add_many(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# print(add_many(1, 2))           # 3
# print(add_many(1, 2, 3, 4, 5))  # 15

# # 3-2. 연산자를 더하기와 곱하기로 구분하여 인자를 계산하는 함수
# def add_mul(choice, *args):
#     '''연산자와 숫자를 입력받아 계산된 결과를 반환하는 함수

#     Args:
#         choice (str) : add | mul
#         *args : 가변 인자 

#     Return:
#         result : *args값들을 choice로 연산한 결과'''

#     if choice == "add": 
#         result = 0
#         for i in args:
#             result += i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result *= i
#     return result

# print(add_mul('add', 1,2,3,4,5))    # 15
# print(add_mul('mul', 1,2,3,4,5))    # 120
#endregion

#region 4. 키워드 파라미터 kwargs
# def print_kwargs(**kwargs):         # **을 붙이면 매개변수 kwargs는 딕셔너리가 되고 모든 key=value 형태의 결괏값이 그 딕셔너리에 저장된다.
#     print(kwargs)                   # 모두 딕셔너리로 만들어져서 출력된다

# print_kwargs(a=1)                   # {'a': 1}
# print_kwargs(name='foo', age=3)     # {'name': 'foo', 'age': 3}
#endregion

#region 5. python의 함수는 일급 객체
# # 5-1. 함수를 변수에 저장 가능
# def hello():
#     print('Hello')

# hi = hello
# hi()
# print(type(hi))

# # 5-2. 사칙연산 함수 
# def add(a, b):
#     return a+b
# def subtract(a, b):
#     return a-b

# def calc(func, a, b):
#     print(f'{func.__name__} 계산 결과: {func(a,b)}')

# calc(add, 3, 4)
# calc(subtract, 3, 4)
#endregion

#region 6. 함수의 결괏값은 언제나 하나
# def add_and_mul(a,b):
#     return a+b, a*b

# print(add_and_mul(5, 10))       # (15, 50) -> 함수의 결과값은 하나이기 때문에 튜플이 생성되어 반환됨.
# sum, mul = add_and_mul(5, 10)
# print(sum, mul)                 # 15 50
#endregion

#region 7. 람다(lambda) 식
# lambda는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할
# def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰인다.
# lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식

add = lambda a, b: a+b
subtract = lambda a, b: a-b
def calc(operator, func, a, b):
    print(f'{a}와 {b}의 {operator} 결과: {func(a, b)}') 

calc('덧셈', add, 3, 4)
calc('뺄셈', subtract, 3, 4)
calc('곱셈', lambda a, b: a*b, 3, 4) 
calc('나눗셈', lambda a, b: a/b, 3, 4)
#endregion








