'''
F-string()
문자열과 변수를 혼합하여 사용할 대 작성
문법:F"문자열 변수"


'''

day="수요일"
str=f"오늘은 {day} 입니다"
print(str)

age=13
name="아인"
str=f"저는 {age}살이고 이름은 {name}입니다"
print(str)

age=40
name="윤성"
str=f"저는 {age}살이고 이름은 {name}입니다"
print(str)

season="봄"
day=18
month=4
str=f"오늘의 계절은 {season}이고 {month}월 {day}일입니다"
print(str)

num1=100
num2=200
str=f"첫번째 숫자는 {num1}이고 두번재는 {num2}이다, 두수합은 {num1+num2}이다"
print(str)