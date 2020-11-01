#region if ~ else문
num = int(input("정수를 입력하세요: "))

# 1. num이 짝수인지 검사
if num%2==0:
    print('짝수')
else:
    print('홀수')

# 2. num이 양수이고, 짝수인지 검사
if num>0:
    if num%2==0:
        print('짝수')
    else:
        print('홀수')
else:
    print('자연수를 입력하세요.')

# # 3. 현금 또는 카드
card = False
cash = 2000
if cash >= 3000 or card:
    print('택시 탑승 가능')
else:
    print('걸어가야함')

# # 4. x in 리스트, 튜플, 문자열
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print('택시 탑승 가능')
else:
    print('걸어가야함')

# # 5. elif
pocket = ['paper', 'cellphone', 'money']
card = True

if 'money' in pocket:
    print('돈이 있다.')
elif card:
    print('카드가 있다.')
else:
    print('아무것도 없다.') 

# 6. 조건부 표현식
score = int(input('당신의 점수는: '))

# if score >= 60:
#     message = "success"
# else:
#     message = "failure"

message = "success" if score >= 60 else "failure"

print(message)

    
#endregion






