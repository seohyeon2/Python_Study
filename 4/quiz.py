# Quiz) 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 주는 추첨 프로그램을 작성하시오

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 활용

# 출력 문장  : -- 당첨자 발표 --
#              치킨 당첨자 : 1
#              커피 당첨자 : [2, 3, 4]
#              -- 축하 합니다 --

# 활용 예제
'''
from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst,1))
'''

from random import *
#id_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

id_list = range(1,21) # 1부터 20까지 숫자를 생성
id_list = list(id_list)
shuffle(id_list)

winner = sample(id_list,4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winner[0]))
print("커피 당첨자 : {0}".format(winner[1:]))
print("-- 축하 합니다 --")