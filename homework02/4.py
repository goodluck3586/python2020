#region 4. 성적 처리기 

# 입력: 학생 이름을 문자열로 입력, 중간고사, 기말고사, 과제 성적을 정수형으로 입력
# 출력: 학생이름, 계산된 합계, 계산된 평균
#endregion

# 학생 클래스 정의
class Student:
    def __init__(self, name, midScore, finalScore, projectScore):
        self.name = name
        self.midScore = midScore
        self.finalScore = finalScore
        self.projectScore = projectScore
    
    def get_name(self):
        return self.name
    
    def get_sum(self):
        return self.sum

    def get_avg(self):
        return self.avg

    def calculate(self):
        self.sum = self.midScore + self.finalScore + self.projectScore
        self.avg = self.sum / 3

# 필요한 데이터 입력 받기
name = input('이름 입력: ')

midScore = int(input('중간 고사 성적 입력: '))
finalScore = int(input('기말 고사 성적 입력: '))
projectScore = int(input('과제 성적 입력: '))

# 학생 객체 생성
student1 = Student(name, midScore, finalScore, projectScore)

# 합계와 평균 계산 및 출력
student1.calculate()

print('\n학생 이름: ', student1.get_name())
print('합계: ', student1.get_sum())
print('평균: ', student1.get_avg())
