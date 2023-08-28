# 얕은 복사(Shallow Copy)
# : 원본 객체의 주소 값을 복사
# '=' 연산자
# copy 모듈의 copy() 함수

import copy

origin_list = [1,2,3]
copy_list_a = origin_list
copy_list_b = origin_list.copy()

copy_list = origin_list

print(id(origin_list))
print(id(copy_list))

print(origin_list)
print(copy_list)

copy_list[0] = 5
print(origin_list)
print(copy_list)

# 원본 리스트와 복사된 리스트가 같은 주소를 가지고 같은 객체를 가리킴
# 따라서 복사된 리스트를 변경하면 원본 리스트 또한 변경.
# 불변형(immutable) 객체에서는 복사한 객체에 데이터를 변경해도 원본 객체에 영향이 없지만,
# 리스트와 같은 변형(mutable) 객체에서는 복사한 객체의 변경이 원본 객체에도 영향을 미친다.