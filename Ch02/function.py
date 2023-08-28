#대소문자 바꾸기 - upper, lower
#upper() 문자열 알파벳 -> 대문자
#lower() 문자열 알파벳 -> 소문자

#문자열 공백 제거 - strip, lstrip, rstrip
#strip() : 문자열 양옆의 공백 제거
#lstrip() : 왼쪽 공백 제거
#rstrip() : 오른쪽 공백 제거

#문자열 구성 파악 : isxx()
#xx로 구성되어 있는가 true/false
#isalnum() : 알파벳 or 숫자
#isalpha() : 알파벳
#isidentifier() : 식별자
#isdecimal() : 정수 형태
#isdigit() : 숫자로 인식
#isspace() : 공백
#islower() : 소문자
#isupper() : 대문자

#문자열 찾기 : find(), rfind(), in 연산
#find() : 왼쪽부터 찾아서 처음 등장하는 위치 인덱스 반환
#rfind() : 오른쪽부터 찾아서 처음 등장하는 위치 인덱스 반환
#in : 문자열 내부에 특정 문자열이 있는지 확인하여 True, False 값 반환

#문자열 자르기 : split
#문자열을 특정한 문자로 자름
#실행 결과로 리스트 반환
a = "10 20 30 40 50".split(" ")
print(a)