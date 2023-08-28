# format()
# 중괄호를 포함한 문자열 뒤에 마침표(.)를 찍고 사용
# 중괄호 개수와 format 함수 괄호 안 매개변수 수는 반드시 같아야함.
format_a = "{}만 원".format(5000)
format_b = "{} {} {}".format(1,"문자열",True)

print(format_a)
print(format_b)

# 정수를 특정 칸에 출력
output_a = "{:d}".format(52)
print(output_a)

output_b = "{:5d}".format(52)
print(output_b)

output_c = "{:05d}".format(52)
output_d = "{:05d}".format(-52)
print(output_c)
print(output_d)

#기호를 붙여 출력
outpuc_a = "{:+d}".format(52)
outpuc_b = "{:-d}".format(52)
outpuc_c = "{: d}".format(52)
outpuc_d = "{: d}".format(52)
print(outpuc_a)
print(outpuc_b)
print(outpuc_c)
print(outpuc_d)

#조합
output_a = "{:+5d}".format(52)
output_b = "{:=+5d}".format(52)
output_c = "{:+05d}".format(52)
print(output_a)
print(output_b)
print(output_c)

#float
output_a = "{:f}".format(52.273)
output_b = "{:+15f}".format(52.273)
output_c = "{:+015f}".format(52.273)
print(output_a)
print(output_b)
print(output_c)

#소수점 아래 자릿수 지정
output_a = "{:15.3f}".format(52.273)
output_b = "{:15.2f}".format(52.273)
output_c = "{:15.1f}".format(52.273)
print(output_a)
print(output_b)
print(output_c)

#의미 없는 소수점 제거
output_a = 52.0
output_b = "{:g}".format(output_a)
print(outpuc_a)
print(outpuc_b)