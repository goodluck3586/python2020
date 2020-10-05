# # 1. 파일 쓰기
# f = open("새파일.txt", 'w', encoding='utf-8')     # r: 읽기 모드, w: 쓰기 모드, a: 추가 모드
# f.write('Hello world\n')
# f.write('안녕하세요\n')
# f.close()

# # 2. 파일을 쓰기 모드로 열어 출력값 작성하기
# f = open("새파일.txt", 'w', encoding='utf-8')
# for i in range(1, 6):
#     f.write(f"{i} 번째 줄입니다.\n")
# f.close()

# # 3. 새로운 내용 추가하기
# f = open("새파일.txt", mode="a", encoding="utf-8")
# for i in range(6, 11):
#     f.write(f"{i} 번재 줄입니다.\n")

# # 4. 파일 한 줄 읽기
# f = open("새파일.txt", mode="r", encoding="utf-8")
# print(f.readline(), end='') # 1 번째 줄입니다.
# print(f.readline(), end='')
# f.close()

# 5. 파일 여러 줄 읽기
# f = open("새파일.txt", mode="r", encoding="utf-8")
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line, end='')
# f.close()

# f = open("새파일.txt", mode="r", encoding="utf-8")
# for line in f.readlines():
#     print(line, end='')
# f.close()

# # 6. 파일 전체 내용 읽기
# f = open("새파일.txt", mode="r", encoding="utf-8")
# print(f.read())     # f.read()는 파일의 내용 전체를 문자열로 돌려준다.
# f.close()

# # 7. with문 사용하여 파일 읽기(자동으로 자원을 닫아준다.)
# with open("새파일.txt", mode="r", encoding="utf-8") as f:
#     print(f.read())

# # 8. 파일 복사(특정 단어 바꾸기도)
with open("새파일.txt", mode="r", encoding="utf-8") as f1, open("새파일2.txt", mode="w", encoding="utf-8") as f2:
    f2.write(f1.read().replace("줄", "line "))

