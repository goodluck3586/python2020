#region 매개 변수가 없는 생성자
class Calculator1:
    # 생성자: 클래스 객체를 생성하는 함수
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result

# 객체 생성
calc1 = Calculator1()
calc2 = Calculator1()

print(calc1.add(1))  # 1
print(calc1.add(2))  # 3
print(calc2.add(3))  # 3
print(calc2.add(4))  # 7
#endregion

#region 매개 변수가 있는 생성자를 가진 클래스
# 덧셈을 수행하는 객체 또는 곱셈을 수행하는 객체
class Calculator2:
    def __init__(self, operator):
        self.operator = operator
    
    def calc(self, *args):  # *args => 여러개의 인자를 튜플로 받는 매개변수
        if self.operator == 'add':
            # 모든 args의 값 덧셈 수행
            self.result = 0
            for i in args:
                self.result += i
        elif self.operator == 'multiply':
            self.result = 1
            # 모든 args의 값 곱셈 수행
            for i in args:
                self.result *= i
        return self.result

calc3 = Calculator2('add')
print(calc3.calc(1,2,3,4,5))
print(calc3.result)

calc4 = Calculator2('multiply')
print(calc4.calc(1,2,3,4,5))
print(calc4.result)

#endregion

#region 사칙연산 클래스
# 생성자에 숫자 두 개를 받아서, 사칙연산 메소드를 수행하는 클래스 add, subtract, multiply, divide
class Calculator3:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

# calc = Calculator3(3, 4)
# print(calc.add())
# print(calc.subtract())
# print(calc.multiply())
# print(calc.divide())
#endregion

#region 상속
class ExtendedCalcultor(Calculator3):
    def pow(self):
        return self.num1 ** self.num2

calc = ExtendedCalcultor(2, 4)
# print(calc.add())
# print(calc.subtract())
# print(calc.multiply())
# print(calc.divide())
# print(calc.pow())
#endregion

#region 메소드 오버라이딩
class SafeCalculator(Calculator3):
    def divide(self):
        if self.num2 == 0:
            return '0으로 나눌 수 없습니다!!!'
        else:
            return self.num1 / self.num2

calc = SafeCalculator(5, 0)
print(calc.divide())

calc = SafeCalculator(5, 2)
print(calc.divide())
#endregion

#region 클래스 변수
class Family:
    lastname = '이'

    def __init__(self, firstname):
        self.firstname = firstname

dongyun = Family('동윤')
print(f"{dongyun.lastname}{dongyun.firstname}")  # 이동윤

jimin = Family('지민')
print(f"{jimin.lastname}{jimin.firstname}")  # 이지민
#endregion

























