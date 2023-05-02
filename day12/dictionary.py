'''
딕셔너리
파이선에서 사용하는 자료구조
key랑 value이 상으로 존재
문법: 중괄호,:사용
indexing가능(key사용)
indexing method 이용가능(키)
key와 value상을 추가하는 반법
1indexing이용
삭제하는법
1del 이용

dict구조안에 key가 들어잇는지 확인할때 "key in dict" 사용

'''

# height={'윤성':145,'도윤':158,'아인':151}
# height["도윤"]=185

# height.update({"윤성":195})

# height["선새님"]=178

# height.update({"보리":50})

# del height["선새님"]
# print(height)

# del height["보리"]
# print(height)
# print(height.get('아인'))
# print(height['아인'])

# print("윤성이가 말했다.'왜?'")

# a=[10,20,30]
# a.append

# height={'윤성':145,'도윤':158,'아인':151}
# height["도윤"]=185

# print("윤성" in height)

# print("보리" in height)

# print(height.key())
# print(height.ualues())

fruits={"오랜지":50,"바나나":100,"사과":250}
fruit=input("과일가게 입니다! 무엇을 원하나요?:")
print(f"우린{fruit}가 있어!!,{fruits[fruit]}개 정도 남았어!")