#region 5. 설정시간 알리미
# 입력: "시:분"초" => 상대 시각으로 표시된 알람 시간
# 출력: 입력 요구 메시지, 현재 시간, 알람 소리, 오류 발생 시 오류 메시지
#endregion

import time
import winsound

# 현재 시간을 '시:분:초' 형식으로 출력한다.
print(f'현재 시간: {time.strftime("%H:%M:%S")}')
alarm_time = input("알람 시간: ")                  # 알람 시간을 '시:분:초' 형식으로 입력받느다.

alarm_hms = alarm_time.split(':')
if len(alarm_hms) == 3 and 0<=int(alarm_hms[0] \
    and 0<=int(alarm_hms[1]) and 0<=int(alarm_hms[2])):
    # 알람 시간만큼 대기한 후 알람 소리 재생
    time.sleep(int(alarm_hms[0])*60*60 \
        + int(alarm_hms[1])*60 + int(alarm_hms[2]))
    for i in range(1, 10):
        winsound.Beep(i*100, 200)
        
else:
    print('입력한 알람 시간 형식에 오류가 있습니다.')   # 알람 시간이 올바르지 않다면 오류 메시지를 출력하고 종료한다.

























