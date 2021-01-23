#region if ~ else문
num = int(input('정수를 입력하세요: '))  # 형 변환

# 1. num이 짝수인지 홀수인지 출력
if num % 2 == 0:
    print('짝수')
else:
    print('홀수')

# 2. num이 양수이면 => 짝수/홀수 출력, 음수이면 => '양수 입력!!!'
if num>0:
    if num%2==0:
        print('짝수')
    else:
        print('홀수')
else:
    print('양수 입력!!!')

# 3. 택시 탑승(현금 또는 카드 보유 체크)
card = False
money = 2000

if money>=3000 or card:
    print('택시 탑승 가능')
else:
    print('걸어가야함')

# 4. x in 리스트/튜플/문자열
pocket = ['paper', 'cellphone']

if 'money' in pocket:
    print('택시 탑승 가능')
else:
    print('걸어가야함')

# 5. elif
pocket = ['paper', 'cellphone', 'money']
card = True

if 'money' in pocket:
    print('돈이 있음')
elif card:
    print('카드 있음')
else:
    print('아무것도 없음')

# 6. 조건부 표현식
score = int(input('당신의 점수는? '))

if score >= 60:
    message = 'success'
else:
    message = 'failure'

message = 'success' if score >= 60 else 'failure'

print(message)



