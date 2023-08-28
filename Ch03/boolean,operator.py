#boolean
#True, False 값
#True, False 첫 글자는 반드시 대문자

#comparison operator
#== 같다
#!= 다르다
#< 작다
#<= 작거나 같다
#> 크다
#>= 크거나 같다
x = 25
print(10 < x < 30)
print(40 < x < 60)

#logical operator
#1. not 연산자
#단항 연산자
#True, False가 서로 바뀜
x = 10
under_20 = x < 20
print("under_20 : ", under_20)
print("not under_20 : ", not under_20)

#2. and 연산자
#이항 연산자
#양쪽 값이 모두 참일 때만 True
#True True = True
#True False = False
#False True = False
#False False = False

#2. or 연산자
#이항 연산자
#둘 중 하나만 참이어도 True
#True True = True
#True False = True
#False True = True
#False False = False