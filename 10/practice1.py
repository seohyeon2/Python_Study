# <모듈_사용>

# import로 모듈 사용
'''
import practice1_module
practice1_module.price(3) # 3명이서 영화 보러 갔을 때 가격
practice1_module.price_morning(4) # 4명이서 조조 영화 보러 갔을 때 가격
practice1_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때 가격
'''

# import 모듈 별명으로 호출
'''
import practice1_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)
'''

# from으로 모든 모듈 사용
'''
from practice1_module import *
price(3)
price_morning(4)
price_soldier(5)
'''

# from으로 특정 모듈만 사용
''''
from practice1_module import price, price_morning
price(3)
price_morning(4)
#오류 : price_soldier(5)
'''

# from 모듈 별명으로 호출
from practice1_module import price_soldier as ps
ps(3)