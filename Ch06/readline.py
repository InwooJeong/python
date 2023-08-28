import sys

# 1. 문자열 입력 받을 때
str = sys.stdin.readline()
# 문자열에 개행문자(\n)이 기본으로 추가됨

# 2. 한 개의 정수를 입력 받을 때
str2 = int(sys.stdin.readline())

# 3. 정해진 개수의 정수를 입력 받을 때
a, b = map(int, sys.stdin.readline().split())

# 4. 임의 개수의 정수를 입력 받을 때
data = list(map(int, sys.stdin.readline().split()))

# 5. N줄의 문자열을 입력 받아 리스트에 저장
n = int(sys.stdin.readline())
data = [sys.stdin.readline().split() for i in range(n)]