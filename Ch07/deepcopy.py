# 깊은 복사(Deep Copy)
# :참조 주소 값이 아닌 참조된 객체 자체를 복사
# copy 모듈의 deepcopy() 함수
# list slicing [:]

import copy

origin_list = [1,2,3]

copy_list_a = copy.deepcopy(origin_list)
copy_list_b = origin_list[:]

origin_list = [1,2,3]
copy_list = origin_list[:]

print(id(origin_list))
print(id(copy_list))

print(origin_list)
print(copy_list)

copy_list[0] = 5
print(origin_list)
print(copy_list)

# 원본 리시트와 복사된 리스트는 각기 다른 객체
# 복사된 리스트를 변경해도 원본 리스트는 변화가 없다.

# 1차원 리스트 깊은 복사
origin_list = [1,2,3]

# deepcopy()
copy_list_a = copy.deepcopy(origin_list)
# list slicing
copy_list_b = origin_list[:]

# 2차원 리스트 깊은 복사
origin_list = [[1,2,3],[4,5,6],[7,8,9]]

#deepcopy()
copy_list_a = copy.deepcopy(origin_list)

#list slicing
copy_list_b = [item[:] for item in origin_list]