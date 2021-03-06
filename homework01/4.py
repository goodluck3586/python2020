#region 4. 도서 게임기
# 도서 데이터: (도서명, 저자, 출판사, 가격, 출판년도, 키워드 등)

# 입력: 도서 정보
# 출력: 검색한 도서의 정보
# 처리: 도서 정보가 저장된 딕셔너리에서 원하는 도서 찾기
#endregion

books = [
    {"도서명": "안드로이드앱개발", "저자": "최전산", "출판사": "한빛", "가격": 25000, "출판년도": 2017},
    {"도서명": "파이썬", "저자": "강수라", "출판사": "연두", "가격": 23000, "출판년도": 2019},
    {"도서명": "파이썬", "저자": "이동윤", "출판사": "한빛", "가격": 33000, "출판년도": 2020}
]
choice = 0      # 검색 방법 선택 변수
kwd = ""        # 검색 방법에 대한 딕셔너리 키값 변수
find = 0        # 도서가 찾아지면 1, 못 찾으면 0

while True:
    # 도서명, 저자, 출판사 중 검색할 수 있는 방법 제시 -> 사용자 선택 입력받기
    choice = '1'
    choice = input('''도서 검색 키워드 선택
    1. 제목
    2. 저자
    3. 출판사
    4. 끝내기
    선택(1, 2, 3) : ''')

    # 사용자 선택에 따라 검색 키워드 입력 받기
    if choice == '1':
        kwd = '도서명'
    elif choice == '2':
        kwd = '저자'
    elif choice == '3':
        kwd = '출판사'
    elif choice == '4':
        break
    else:
        print('잘못된 입력값 입니다.')

    userin = input('검색 키워드를 입력하시오: ')
    find = False

    # 키워드를 이용해 저장된 데이터에서 찾기 -> 찾은 도서 정보 출력
    for book in books:
        if userin == book[kwd]:
            print("도서명: ", book["도서명"])
            print("저  자: ", book["저자"])
            print("출판사: ", book["출판사"])
            print("가  격: ", book["가격"])
            print("-" * 30)
            find = True
    
    if find == False:
        print("검색한 도서가 없습니다.")
