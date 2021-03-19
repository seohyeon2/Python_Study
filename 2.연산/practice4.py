# <랜덤함수>

# random 라이브러리 이용
from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random()*10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random()*10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random()*10)+1) # 1 ~ 10 이하의 임의의 값 생성

# ex) 로또번호 추출
print(int(random()*45)+1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random()*45)+1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random()*45)+1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random()*45)+1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random()*45)+1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random()*45)+1) # 1 ~ 45 이하의 임의의 값 생성

print(randrange(1,46)) # 1~ 46 미만의 임의의 값 생성

print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성