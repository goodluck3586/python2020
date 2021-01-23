#region 2. 숫자 추측 게임기 : 1~30 사이의 임의의 숫자 맞히기
# 규칙 추측 횟수 제한 5회, 제한 횟수 내에 맞히면 횟수를 1감소하고, 틀리면 1 증가시킴
# 입력: 사용자가 추측한 숫자, 게임 지속 요부 yes, no
# 처리: 추측한 숫자와 정답 비교
# 출력: 정답 여부, 추측한 숫자보다 정답이 큰지 작은지
#endregion

import random

print('숫자 추측 게임(1~30 사이의 숫자)')
ansNumber = random.randint(1, 30)

count = 1
limit = 5
playAgain = 'yes'

# 정답을 맞추거나 count가 limit를 초과하면 반복 멈추기
while playAgain == 'yes':
    print(f'{limit}번 만에 맞혀야됩니다.')
    count = 1
    guessNumber = -1
    while guessNumber != ansNumber and count <= limit:
        guessNumber = int(input("숫자를 입력하시오: "))

        if guessNumber == ansNumber:
            break
        elif guessNumber < ansNumber:
            print('Up')
        else:
            print('Down')
        count += 1

    if guessNumber == ansNumber:
        print(f'\n{count}번 만에 정답을 맞혔습니다. 축하해요 \n')
        if limit > 1:
            limit -= 1
    else:
        print(f'\n정답은 {ansNumber} 입니다.\n')
        limit += 1

    playAgain = input('게임을 다시 할까요?(yes or no) :')
    ansNumber = random.randint(1, 30)

print('게임이 종료되었습니다.')
    











