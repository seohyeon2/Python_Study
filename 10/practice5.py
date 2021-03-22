# <내장함수>

#참고: https://docs.python.org/3/library/functions.html

# input : 사용자 입력을 받는 함수
'''
lang = input("무슨 언어를 좋아하세요?")
print("{0}은 아주 좋은 언엉비니다!".format(lang))
'''

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())

import random #외장 함수
print(dir())

import pickle
print(dir())

print(dir(random)) # => 랜덤에서 사용할 수 있는 것들 나옴

lst = [1,2,3]
print(dir(lst)) # => 리스트에서 사용할 수 있는 것들 나옴

name = "psh"
print(dir())