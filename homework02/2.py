#region 2. 토익 점수 분석기
# 규칙 추측 횟수 제한 5회, 제한 횟수 내에 맞히면 횟수를 1감소하고, 틀리면 1 증가시킴

# 입력: 사용자가 추측한 숫자, 게임 지속 요부 yes, no
# 출력: 정답 여부, 추측한 숫자보다 정답이 큰지 작은지
#endregion

# 토익점수 빈도수 반환 함수 
def frequency(toeicScores):
    # 0점 ~ 900 점대의 빈도수 저장 리스트
    counters = [0,0,0,0,0,0,0,0,0,0]    
    for score in toeicScores:
        counters[score//100] += 1   # 100으로 나눈 정수몫
    return counters

# 최대 빈도수의 점수대와 개수 반환 함수
def max_frequency(counters):
    max = 0
    scoreBase = 0
    N = len(counters)

    # 빈도수가 가장 많은 점수대의 개수(max)와 점수(scoreBase) 저장
    for i in range(N):
        if max < counters[i]:
            max = counters[i]
            scoreBase = i * 100
    return scoreBase, max

# 최소 빈도수의 점수대와 개수 반환 함수
def min_frequency(counters):
    min = 11
    scoreBase = 0
    N = len(counters)

    # 빈도수가 가장 많은 점수대의 개수(max)와 점수(scoreBase) 저장
    for i in range(N):
        if counters[i] != 0 and min > counters[i]:
            min = counters[i]
            scoreBase = i * 100
    return scoreBase, min

# 토익 점수 리스트
toeicScores = [510, 630, 750, 780, 620, 805, 890, 650, 840, 670]

# 토익점수대별 빈도수 구하기
counters = frequency(toeicScores)

# 최대 빈도수의 점수대와 개수 출력
scoreBase, maxCount = max_frequency(counters)
print(f'가장 많은 점수대={scoreBase}, 빈도수={maxCount}')

# 최소 빈도수의 점수대와 개수 출력
scoreBase, minCount = min_frequency(counters)
print(f'가장 많은 점수대={scoreBase}, 빈도수={minCount}')




