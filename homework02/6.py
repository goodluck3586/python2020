import random

# 단어장 객체
class Vocabulary:
    # 단어장 만들기
    def __init__(self, wdict):
        self.words = wdict.copy()
        self.untrained = set(self.words)    # 단어 딕셔너리 -> 집합 변환
        self.renew()
    
    # 집합을 리스트로 변환하여 섞기
    def renew(self):
        self.target = list(self.untrained)  # 집합 -> 리스트 변환
        random.shuffle(self.target)         # 리스트 요소 섞기
        self.untrained = set()              # untrained 집합을 빈 집합으로 만들기

    # 단어 리스트 반환
    def target_keys(self):
        return self.target

    # 사용자의 입력이 맞는지 확인하는 함수
    def check(self, key, value=None):           # key = 뜻, value = 철자
        # 사용자가 입력한 key값이 없는 경우
        if key not in self.words:
            return None
        
        # 사용자가 입력한 value값이 None이 아닌 경우
        if value is not None:
            # 철자 검사
            if self.words[key] == value:
                return Ellipsis
            self.untrained.add(key)     # 틀린 경우 untrained집합에 '단어의 뜻' 추가
        return self.words[key]          # 단어의 철자 리턴
    
    # 랜덤하게 단어 순서를 섞는 함수
    def shuffle(self):
        random.shuffle(self.target)

#region 단어장 입력 받기
wdict ={}
while True:
    line = input("등록/암기할 단어의 철자와 뜻 : ")
    tokens = line.split()
    if len(tokens) != 2:
        break
    wdict[tokens[1]] = tokens[0]
#endregion

voc = Vocabulary(wdict)

# 단어 리스트에 단어가 존재하는 경우 반복
while len(voc.target_keys()) > 0:
    print('\n암기할 단어 : ', voc.target_keys())
    nQNA = int(input('단어별 문답 횟수: '))
    print()

    # 문답 개수만큼 반복
    for index in range(nQNA):
        voc.shuffle()   # 단어장 무작위로 섞기
        for meaning in voc.target_keys():
            answer = input(f"'{meaning}'의 뜻을 가진 단어는? ")
            word = voc.check(meaning, answer)
            if word is Ellipsis:
                print('정답입니다.')
            else:
                print(f'틀렸습니다. 정답은 {word} 입니다.')
    voc.renew()     # 순회 집합 갱신

print('\n단어 학습이 끝났습니다.')
