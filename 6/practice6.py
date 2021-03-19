# <지역변수와 전역변수>

# 지역변수란? 함수 내에서만 사용하는 변수
# 전역변수란? 모든 공간에서 사용하는 변수

'''
gun = 10

def checkpoint(soldiers): #경계근무
    gun = 20 #지역변수
    gun = gun - soldiers
    print("[함수 내] 남은총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) #2명이 경계 근무 나감
print("남은총 : {0}".format(gun))
'''

gun = 10

def checkpoint(soldiers): #경계근무
    global gun #전역 공간에 있는 gun 사용 
    gun = gun - soldiers
    print("[함수 내] 남은총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) #2명이 경계 근무 나감
print("남은총 : {0}".format(gun))


# 파라미터 사용
gun = 10

def checkpoint_ret(gun,soldiers): #경계근무
    gun = gun - soldiers
    print("[함수 내] 남은총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun,2)
print("남은총 : {0}".format(gun))