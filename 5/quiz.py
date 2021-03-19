# Quiz) 택시기사에게 50명의 승객과 매칭기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해짐
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 함

# 출력 문장  
# [o] 1번째 손님 (소요시간 : 15분) 
# [ ] 2번째 손님 (소요시간 : 50분) 
# [o] 3번째 손님 (소요시간 : 5분) 
# ...
# [ ] 50번째 손님 (소요시간 : 16분) 
#
# 총 탑승 승객 : 2명

from random import *

total = 0

for customer in range(1,51):
    time = randint(5,50)
    if(time > 15 ): 
        print("[ ]  {0}번째 손님 (소요시간 : {1}분)".format(customer,time))
    else : 
        print("[o]  {0}번째 손님 (소요시간 : {1}분)".format(customer,time))
        total += 1
print("총 탑승 승객 : {0}명".format(total))