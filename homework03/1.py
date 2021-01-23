import turtle as t
from random import *

# 리스트에 가위, 바위, 보 이미지 파일을 저장
s = ["C:/Repository/python2020/homework03/images/pap.gif", "C:/Repository/python2020/homework03/images/sci.gif", "C:/Repository/python2020/homework03/images/roc.gif"]
t.setup(300, 300)

# 가위, 바위, 보의 이미지를 터틀이 가질 수 있는 모양으로 등록한다.
for img in s:
    t.addshape(img)
print("가위바위보를 하려면, 가위는 s, 바위는 r, 보는 p를 누르세요.")

# 0=보, 1=가위, 2=바위 0(보)<1(가위)2(바위)
def show_result(myno, cno):
    t.shape(s[cno])             # 난수에 저장된 이미지 파일을 가져와 화면에 출력
    result = myno - cno         # 우승 계산하기 (-2 ~ 2가 나오게 된다.) 

    # 0=무승부, (-2, 1)=이긴 경우, (2, -1)=진 경우
    if result == 2: 
        result = -1
    elif result == -2: 
        result = 1
    if result == 0:
        print('컴퓨터와 무승부입니다. 다시 하세요.')
    elif result < 0:
        print("당신이 졌습니다.")
    else:
        print("당신이 이겼습니다.")

# 사용자의 입력에 따라 호출되는 함수
def rock():
    cno = randint(0, 2)     # 컴퓨터는 0, 1, 2 사이의 난수를 발생
    myno = 2
    print("당신의 선택은 [바위].", end=' ')
    show_result(myno, cno)  # 사용자가 이겼는지 컴퓨터가 이겼는지를 비교하는 함수를 호출하여 계산

def scissor():
    cno = randint(0, 2)
    myno = 1
    print("당신의 선택은 [가위].", end=' ')
    show_result(myno, cno)

def paper():
    cno = randint(0, 2)
    myno = 0
    print("당신의 선택은 [보].", end=' ')
    show_result(myno, cno)

# 사용자의 입력값에 해당하는 함수를 호출하여 사용자의 입력값과 컴퓨터가 선택한 이미지 값을 설정한다.
# 사용자로부터 r, s, p 중에 하나의 값을 입력받는다.
t.onkeypress(rock, 'r')     # 'r'키를 누르면 rock() 함수 실행
t.onkeypress(scissor, 's')   
t.onkeypress(paper, 'p')     

t.listen()
t.mainloop()

