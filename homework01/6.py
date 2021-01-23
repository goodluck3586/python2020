#region 6. 간단한 계산기
'''규칙
 - 모든 명령 작업은 한 줄의 텍스트로 구성(연산자 + ' ' + 한자리 숫자)
 - 연산자(+, *, /, %)
'''
# 입력: 규정된 형태의 작업 명령(계산 명령, 치환 명령, 종료 명령)
# 출력: 계산된 값
#endregion

# 입력된 작업이 '계산 명령'일 경우, 해당 연산을 적용 누적시킨다.
# 입력된 작업이 '치환 명령'일 경우, 지정된 값을 누적 변수로 참조할 수 있게 설정한다.
# 입력된 작업이 '종료 명령'일 경우, 반복을 끝낸다.
# 입력된 작업이 잘못된 경우 오류 메시지를 출력한다.

value = 0
while True:
    print("\n 현재 값 : ", value)
    line = input("작업 명령 입력 : ")
    tokens = line.split()   # 공백으로 분리
    if len(tokens) > 0:
        operator = tokens[0]    # 첫 문자는 연산자
        if len(tokens) == 1:    # 하나의 값만 있는 경우 종료 명령인지 확인
            if operator == 'x':
                break
            print('잘못된 작업 명령!!')
        elif len(tokens) == 2:          # 두 개의 값이 있는 경우 두 번째 값은 피연산자
            operand = float(tokens[1])  # 피연산자 저장
            
            if operator == '=':
                value = operand
            elif operator == '+':
                value += operand
            elif operator == '*':
                value *= operand
            elif operator == '/' or operator == '%':
                if operand != 0:
                    if operator == '/':
                        value /= operand
                    else:
                        value %= operand
                else:
                    print('잘못된 작업 명령(0으로 나누기)!!')
            else:
                print('잘못된 작업 명령!!')
        else:
            print('잘못된 작업 명령!!')