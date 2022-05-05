import datetime

current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day

birth_year, birth_month, birth_day = map(int, input('생일 입력> ').split())

# 현재월 > 생월
if current_month > birth_month:
    age = current_year - birth_year

# 현재월 < 생월
elif current_month < birth_month:
    age = current_year - birth_year - 1

# 현재월 == 생월
else:
    
    # 현재일 < 생일
    if current_day < birth_day:
        age = current_year - birth_year - 1
    
    # 현재일 >= 생일
    else:
        age = current_year - birth_year
        
print('만 나이는 %d 입니다.' % age)