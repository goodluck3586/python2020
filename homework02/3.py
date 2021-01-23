#region 3. 시차 계산기
# 입력: 시차
# 출력: 우리나라 시간과 캘리포니아 주의 현재 날짜와 시간
#endregion

import datetime

# 윤년 판별 함수
def is_leap_year(yy):
    return yy % 400 == 0 or (yy % 100 != 0) and (yy % 4 == 0)

# 시차 계산 함수 => 한국의 년, 월, 일, 시, 분과 한국과 캘리포니아의 시차 gap을 받음
def jetlag(yy, mm, dd, hh, mi, gap):
    hh += gap   # 한국 시간에 캘리포니아와의 시차만큼 더해준다.
    # 시간이 음수이면 날짜를 조정(날짜를 전날로 변경, 시간을 양수로 변경)
    if hh < 0:
        dd -= 1
        hh += 24

    # 일이 0이면 달을 전달로 조정
    if dd == 0:
        mm -= 1
        if mm == 0:     # 달이 0이면 전년도로 조정
            mm = 12
            yy -= 1
        # 몇 월인지에따라 30, 31일 중 하나의 날로 저장, 윤년이면 29
        if mm in [4, 6, 9, 11]:
            dd = 30
        elif mm in [1, 3, 5, 7, 8, 10, 12]:
            dd = 31
        else:
            if is_leap_year(yy): dd = 29
            else: dd = 28
    
    date = f'{yy}/{mm}/{dd} {hh}:{mi}'
    return date
        
today = datetime.datetime.now()
gap = int(input("시차(양수/음수) : "))
print(f'한국의 현재 날짜와 시간 : ', today.strftime('%Y/%m/%d %H:%M'))
date = jetlag(today.year, today.month, today.day, today.hour, today.minute, gap)
print('캘리포니아의 현재 날짜와 시간: ', date)