# # 파이썬 예외 처리
# 1. 에러가 발생하는 경우 프로그램이 중지된다.
# n = 4 / 0

#region try, except문의 기본 구조
# try:
#     ...
# except [발생 오류[as 오류 메시지 변수]]:
#     ...
#endregion

# # 2. try ~ except문을 통해 에러가 발생해도 프로그램이 중지되지 않도록 할 수 있다.
# try:
#     n = 4 / 0
# except: 
#     pass  # 아무런 동작도 안하고 넘어가기

# # 3. ZeroDivisionError 예외 처리
# try:
#     n = 4 / 0
# except ZeroDivisionError as e:    # 오류 이름과 일치할 때만 except 블록을 수행
#     print(f"0으로 나눌 수 없습니다. : {e}")

# # 4. IndexError 예외 처리
# try:
#     a = []
#     a[0] = 100
# except ZeroDivisionError as e:    # IndexError 발생
#     print(f"인덱싱 할 수 없습니다. : {e}")

# # 5. Exception 예외 처리
# try:
#     n = 4 / 0
#     idx = []
#     idx[0] = 100
# except Exception as e:
#     print(f"오류 발생 : {e}")    // 먼저 발생하는 오류가 들어옴.

# # 6. try ~ except ~ finally 
# # finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행됨.
# try:
#     f = open("readme.txt", mode="r", encoding="utf-8")
#     #f = open("새파일.txt", mode="r", encoding="utf-8")
#     print(f.read())
#     f.close()
# except Exception as e:
#     print(f"오류 발생 : {e}")
# finally:
#     print('finally 구문 실행')

# # 7. 여러개의 오류처리하기
# # 7-1
# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except IndexError:
#     print("인덱싱 할 수 없습니다.")   

# # 7-2
# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except (ZeroDivisionError, IndexError) as e:
#     print(e)

print('마지막 코드')
