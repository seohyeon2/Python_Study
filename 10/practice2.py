# <패키지>

# ex) 여행사

# [태국]
# import 사용
'''
import practice2_module.thailand # => 모듈, 클래스만 import 가능, 메소드 X
trip_to = practice2_module.thailand.ThailandPackage()
trip_to.detail()
'''
# from 사용
'''
from practice2_module.thailand import ThailandPackage # => 메소드 가능
trip_to = ThailandPackage()
trip_to.detail()
'''

#[베트남]
'''
from practice2_module import vietnam 
trip_to = vietnam.VietnamPackage()
trip_to.detail()
'''


# 패키지 생성 및 사용
#  __all__

'''
from practice2_module import * 
trip_to = vietnam.VietnamPackage()
trip_to.detail()
# => 공개범위가 설정되지 않아 오류
# => __init__ 에서 설정 // setting - linting:Enable 해제 
'''