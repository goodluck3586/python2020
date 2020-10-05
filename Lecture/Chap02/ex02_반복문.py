#region 1. while문
# prompt = """1. Add  2. Del  3. List 4. Quit
# Enter number: """

# number = 0
# while number != 4:
#     print(prompt, end="")
#     number = int(input())
#endregion

#region 2. for문 => for 변수 in 리스트(또는 튜플, 문자열):
# # 2-1. 전형적인 for문
# test_list = ['one', 'two', 'three'] 
# for i in test_list:
#     print(i)

# # 2-2. for문과 range()함수 => 숫자 리스트를 자동으로 만들어 주는 range 함수
# # 1부터 100까지의 합계
# sum = 0
# for i in range(1, 101):
#     sum = sum + i
# print(f'1~100까지의 합: {sum}')

# # 2-3. 구구단
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(format(i*j, "2d"), end=" ")
#     print('')

# # <연습문제 1> 사용자가 희망하는 구구단 출력
# dan = int(input('몇 단을 출력할까요? '))
# for i in range(1, 10):
#     print(f'{dan} * {i} = {format(dan*i, "2d")}')

# # 2-4. for문과 시퀀스 자료형
# # 리스트안의 튜플
# a = [(1,2), (3,4), (5,6)]
# for i in a:         
#     for j in i:
#         print(j)

# # 딕셔너리
# students = [{"홍길동": 100}, {"가제트": 200}, {"가가멜": 300}]

# # for seq in students:
# #     # print(seq)
# #     # print(seq.items())
# #     # print(list(seq.items()))
# #     # print(list(seq.items())[0])
# #     data = list(seq.items())[0]
# #     key = data[0]
# #     value = data[1]
# #     print(f"key: {key}, value: {value}")

# # 시퀀스 요소의 index값을 사용하고 싶을 때
# for index, seq in enumerate(students, start=1):
#     data = list(seq.items())[0]
#     key = data[0]
#     value = data[1]
#     print(f"{index} key: {key}, value: {value}")
#endregion

#region 3. break, continue문

langs = ['한국어', 'English']
for i, s in enumerate(langs, start=1):
    print(f'{i}. {s}')

while True:
    inputNum = input('언어를 선택하세요 : ')

    if not inputNum.isnumeric():
        continue
    inputNum = int(inputNum)
    if 0<inputNum<3:
        break
print(f'사용자가 선택한 언어는 {langs[inputNum-1]}입니다.')

#endregion


