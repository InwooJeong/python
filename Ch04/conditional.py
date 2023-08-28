#if 조건문
# : 조건에 따라 코드를 실행하거나 실행하지 않음

import datetime

now = datetime.datetime.now()
if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다!".format(now.month))
    
if 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다!".format(now.month))

if 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다!".format(now.month))       

if now.month == 12 or 1 <= now.month <= 2:
    print("이번 달은 {}월로 겨울입니다!".format(now.month))
    
number = input("정수 입력 > ") 

last_character = number[-1]
last_number = int(last_character)

#case 1
if last_number == 0 \
    or last_number == 2\
    or last_number == 4\
    or last_number == 6\
    or last_number == 8:
    print("짝수입니다.")
    
#case 2
if last_character in "02468":
    print("짝수입니다.")

#case 3    
if int(number) % 2 == 0:
    print("짝수입니다.")
    
# else 조건문
# : if 조건문 뒤에 사용하며, if 조건문의 조건이 거짓일 때 실행    

# elif 구문
# : 세 개 이상의 조건을 연결
# if 조건 :
# elif 조건 :
# elif 조건 :
# ...
# else : 
#     모든 조건이 거짓

#False로 변환되는 값
# None
# 숫자 0, 0.0
# 빈 컨테이너

#조건문 내부를 미구현
# if number > 0:
#     미구현
# else: 
#     미구현    
#  -> IndentationError 발생    
    
# 1. 0을 넣은 코드
# if number > 0:
#     0
# else:     
#     0
# -> 정상적으로 실행.

# 2. pass 키워드
# if number > 0:
#     pass
# else:
#     pass
# 아무것도 안함. 곧 개발 하겠음

# 3. raise NotImplementedError 오류 발생 시키기
# raise 키워드와 미구현 상태를 표현하는 NotImplementedError를 조합 -> 아직 구현하지 않은 부분이라는 오류 강제 발생
# 코드는 정상적으로 실행되지만, 구현되지 않은 부분에 들어선 순간 NotImplementedError 발생
# if number >0:
#     raise NotImplementedError
# else:
#     raise NotImplementedError