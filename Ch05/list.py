array = [273, 32, 103, "문자열", True, False]
print(array)

# 대괄호에 자료를 쉼표로 구분해서 입력
# 인덱스는 1부터 시작

list_a = [273, 32, 103, "문자열", True, False]
list_a[0] = "변경"
print(list_a)
print(list_a[-1])
print(list_a[-2])
print(list_a[-3])
print(list_a[3])
print(list_a[3][0])

list_b = [[1,2,3],[4,5,6],[7,8,9]]
print(list_b[1])
print(list_b[1][1])

list_c = [1,2,3]
list_d = [4,5,6]
print("list_c + list_d = ",list_c + list_d)
print("list_c * 3 = ",list_c * 3)
print("len(list_c) = ",len(list_c))

#리스트에 요소(Element) 추가
# 1. append()
# 리스트 뒤에 요소를 추가
list_f = [1,2,3]
list_f.append(4)
print(list_f)

# 2. insert()
# 리스트 중간에 요소 추가. 삽입한 위치 요소는 뒤로 하나씩 밀림
# list.insert(위치,요소)
list_g = [1,2,3]
list_g.insert(1,10)
print(list_g)

# 3. extend()
# 한 번에 여러 요소를 추가
# 매개변수로 리스트를 입력하면 원래 리스트 뒤에 매개변수 리스트 요소를 모두 추가
# + 와 entend는 비슷한 형태로 동작
# 리스트 연결 연산자는 비파괴적(원본에 영향 x) - extend는 파괴적
list_h = [1,2,3]
list_h.extend([4,5,6])
print(list_h)

# 리스트 요소 제거
# 1. 인덱스로 제거
# del 리스트명[인덱스]
# pop 함수 : 제거할 위치에 있는 요소를 제거. 매개변수가 없다면 마지막 요소를 제거

# 2. 값으로 제거
# 리스트.remove(값)
# 리스트 내 값이 여러개 존재하면 가장 먼저 발견되는 하나만 제거

# 3. 모두 제거
# clear함수 : 리스트 내부 요소를 모두 제거
# 리스트.clear()

# 리스트 내부에 있는지 확인
# in 연산자 : 특정 값이 리스트 내부에 있는가?
# 값 in list

# not in 연산자 : 리스트 내부에 해당 값이 없는가?
# 값 not in list