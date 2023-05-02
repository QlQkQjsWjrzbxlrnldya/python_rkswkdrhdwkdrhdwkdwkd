'''
imput(입력함수)
python에서 내부로 사용자의 값을 전달할대 사용
엔터가 입력될때까지 기다림
입력받은 값은 항상 문자로 인식함
숫자로 변경하기 위해선 int 함수필요


'''
# for i in range(3):
#     aye=input('나이적어')
#     name=input('이름적어')
#     print(f"{aye}살 {name}님 안열")

# num1=input("첫번째 수:")
# num2=input("두번쩨 수:")
# str=f"첫번째 숫자는 {num1}이고 두번재는 {num2}이다, 두수합은 {int(num1)+int(num2)}이다"
# print(str)

# num1=input("첫번째 수:")
# num2=input("두번쩨 수:")
# str=f"첫번째 숫자는 {num1}이고 두번재는 {num2}이다, 두수합은 {int(num1)+int(num2)}이다"
# print(str)

num1=input("첫번째 수:")
num2=input("두번쩨 수:")
str=f"첫번째 숫자는 {num1}이고 두번재는 {num2}이다, 두수합은 {int(num1)+int(num2)}이다 두수차은 {int(num1)-int(num2)}이다"
print(str)