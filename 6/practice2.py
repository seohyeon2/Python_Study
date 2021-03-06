# <전달값과 반환값>

# 전달값과 반환값
# => def 함수명( 전달값 ):
#       내용
#       return (반환값)

# 입금 함수
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

balance = 0 #잔액
balance = deposit(balance,1000)
print(balance)

# 출금 함수
def whitdraw(balance, money):
    if balance >= money: #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance -money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

balance = 2000 #잔액
balance = whitdraw(balance,1000)
balance = whitdraw(balance,4000)

# 저녁 출금 함수
def whitdraw_night(balance, money):
    commission = 100 # 수수료 100원
    return commission,balance - money - commission # 튜플로 반환

balance = 2000 #잔액
commission, balance = whitdraw_night(balance,500)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission,balance))