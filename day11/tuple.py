'''
<튜플이란?>
파이선에서 사용하는 자료구조 중 하나
List와 비슷
리스트:대괄호
튜플:소괄호

<리스트와 튜플의 공통점과 차이점>

공통점:indexing
무언가를 가르키는것(a의 3번째 프린트)
,slicing
구간을 가르키는것(b의 0번째랑 3번째 프린트)

차이점:
리스트는 mutable 값(변경가능)
튜플은: immutable 값(변경불가능)

'''
a=[1,2,3]
b=(1,2,3)
print(a[:2])
print(b[:2])

c=[1,2,3,]
c[1]=10
c[2]=100
print(c)

d=(1,2,3)
d[2]=10
print(d)