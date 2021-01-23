#region 1. 패턴 퀴즈 게임기
# 입력: 추론한 패턴 숫자 입력
# 출력: 패턴 추론 맞힘 여부, 몇 개를 맞혔는지
#endregion

def patternMatch(pattern, correctAns, wrongAns):
    # pattern의 모든 요소를 한 줄로 출력(마지막 요소 제외)
    for i in range(len(pattern)-1):     
        print(pattern[i], end=" ")
    
    guessAns = int(input("다음 수는 무엇일까요?"))

    # 플레이어가 숫자를 맞혔는지 검사한다.
    if guessAns == pattern[len(pattern)-1]:
        correctAns += 1
        print("잘했어요. 축하해요")
    else:
        wrongAns += 1
        print(f"정답은 {pattern[len(pattern)-1]}")
    
    return correctAns, wrongAns

# 맞힌 개수와 틀린 개수 변수를 0으로 초기화 한다.
correctAns = 0
wrongAns = 0

# 다양한 숫자 패턴 생성
pattern1 = [2, 4, 6, 8]
pattern2 = [13, 16, 19, 22]
pattern3 = [2, 3, 5, 7, 11]
pattern4 = [1, 1, 2, 3, 5, 8]
pattern5 = [31, 28, 31, 30]

# 패턴 추론 게임 함수 호출
correctAns, wrongAns = patternMatch(pattern1, correctAns, wrongAns)
correctAns, wrongAns = patternMatch(pattern2, correctAns, wrongAns)
correctAns, wrongAns = patternMatch(pattern3, correctAns, wrongAns)
correctAns, wrongAns = patternMatch(pattern4, correctAns, wrongAns)
correctAns, wrongAns = patternMatch(pattern5, correctAns, wrongAns)

# 맞힌 개수와 틀린 개수를 알려준다.
print(f'{correctAns + wrongAns}개 패턴 중 {correctAns}개 맞았어요')














