# <연습문제 1> 양의 정수를 입력받아 약수를 출력하시오.

#region 1. 숫자 입력받아 변수에 저장하기
input_num = int(input("Enter a positive integer: "))
print(f'Factors of {input_num}')
#endregion

#region 2. 반복문으로 약수 출력하기
for i in range(1, input_num+1):
    if input_num % i == 0:
        print(i, end=' ')
#endregion

