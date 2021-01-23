#region 3. 구구단 게임기
# 규칙
#  - 2단, 5단을 제외한 임으의 구구단 생성하기
#  - 정해진 시간 안에 문제 풀기
#  - 시간초과나 틀린 경우 실패
#  - 정해진 횟수까지 게임을 반복
# 입력: 구구단 횟수, 구구단 문제 답
# 출력: 구구단 문제, 맞힌 개수와 틀린 개수, 응답 시간 등
#endregion

import random
import time

correntAns = 0
wrongAns = 0
limitTime = 3

count = int(input('몇 번 할까요?'))

while count != 0:
    # 임의의 구구단을 위한 숫자 2개 생성
    a = random.randint(3, 9)
    b = random.randint(3, 9)
    if a==5 or b==5:
        continue

    count -= 1
    startTime = time.time()
    product = int(input(f'{a} * {b} = '))
    endTime = time.time()
    spentTime = endTime-startTime
    print(f'{spentTime : .1f}초 만에 답을 했어요.')

    if product == a*b and spentTime < limitTime:
        print("정답입니다.\n")
        correntAns += 1
    else:
        if product == a*b:
            print('시간 초과로 틀렸습니다.\n')
        else:
            print("틀렸습니다.\n")
        wrongAns += 1

print(f'{correntAns+wrongAns} 번중 {correntAns}번 맞았습니다.')


# 구구단 문제 제시 -> 사용자의 입력 받기

# 정답 유무 확인

# 정해진 게임 횟수에 도달하면 게임을 끝내고 맞힌 개수를 출력한다.