#region while문
# prompt = '''1. ADD  2. Del  3. List 4. Quit
# Enter number:'''

# number = 0
# while number != 4:
#     print(prompt, end='')
#     number = int(input())
#endregion

#region for문 => for 변수 in 리스트/튜플/문자열
# # 2-1. 전형적인 for문
# test_list = ['one', 'two', 'three']
# for i in test_list:
#     print(i)

# # 2-2. for문과 range()함수 => 숫자 리스트를 자동으로 만들어주는 함수
# # 1~100까지의 합계
# sum = 0
# for i in range(1, 101):
#     sum = sum + i
# print(f'1~100까지의 합계는 {sum} 입니다.')

# # 2-3. 구구단
# for dan in range(2, 10):
#     for i in range(1, 10):
#         print(f'{dan} * {i} = {dan*i}')
#     print('') 

# <연습문제 1> 사용자가 희망하는 단을 숫자로 입력하면 해당 구구단 출력

# 2-4. for문과 시퀀스 자료형
# # 리스트안의 튜플
# a = [(1,2), (3,4), (5,6)]
# for i in a:
#     for j in i:  # i => (1,2)
#         print(j)

# 딕셔너리
students = [{'홍길동': 100}, {'가제트': 200}, {'가가멜': 300}]
# for dic in students:
#     # print(dic)
#     # print(dic.items())
#     # print(list(dic.items()))
#     # print(list(dic.items())[0])
#     data = list(dic.items())[0]   # ('홍길동', 100)
#     key = data[0]   # '홍길동'
#     value = data[1] # 100
#     print(f'key: {key}, value: {value}')


# # index 값을 같이 사용하고 싶을 때
# for index, dic in enumerate(students, start=1):
#     data = list(dic.items())[0]   # ('홍길동', 100)
#     key = data[0]   # '홍길동'
#     value = data[1] # 100
#     print(f'{index}. key: {key}, value: {value}')

#endregion

#region break, continue문

langs = ['한국어', 'English']

for i, s in enumerate(langs, start=1):
    print(f'{i}. {s}')

while True:
    inputNum = input('언어의 번호를 입력하세요 : ')

    if not inputNum.isnumeric():
        continue
    inputNum = int(inputNum)
    if 0<inputNum<3:
        break

print(f'사용자가 선택한 언어는 {langs[inputNum-1]} 입니다.')

#endregion

