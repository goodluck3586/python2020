# 변수가 저장한 메모리 주소값 확인하기
a = [1,2,3]
print(id(a))  # 14090184

#region 얉은 복사, 깊은 복사
# 얉은 복사
b = a
print(id(b)) # 14090184

b.append(4)
print(a, b)  # [1, 2, 3, 4] [1, 2, 3, 4]
print(f'a is b : {a is b}')
print(f'a==b : {a==b}')

# 깊은 복사
a = [1,2,3]
b = a[:]
print(f'a is b : {a is b}')  # 주소 비교
print(f'a==b : {a==b}')      # 값 비교

print(a, b)  # [1, 2, 3] [1, 2, 3]
b[0] = 10
print(a, b)  # [1, 2, 3] [10, 2, 3]
#endregion

#region 변수를 만드는 여러가지 방법
a, b = ('python', 'life')  # 튜플로 여러개의 변수에 값 대입 가능
print(a, b)  # python life

a, b = 'node', 'js'  # 튜플은 괄호 생략 가능
print(a, b)  # node js

[a, b] = ['python', 'life']
print(a, b)  # python life

a = b = 'node.js'
print(a, b)  # node.js node.js
#endregion

