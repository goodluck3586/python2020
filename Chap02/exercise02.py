# <연습 문제2> 사용자로부터 자연수를 입력받아 자릿수를 출력하시오.

input_num = int(input('Enter an integer:'))

digits = 0
#region 자릿수 구하기
while input_num != 0:
    input_num = int(input_num / 10)
    digits = digits + 1

print(f'Number of digits: {digits}')
#endregion


