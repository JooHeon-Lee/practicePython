def open_account(): #함수정의 def 하고 함수이름():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance,money): # 입금 함수 잔액,현재입금액 전달 받음 
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance,money): #출금
    if balance >= money: #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance
def withdraw_night(balance,money):
    commission = 100# 수수료 100원
    return commission, balance - money - commission # 2개의 값을 콤마로 구분후 반환

balance = 0 # 잔액
balance = deposit(balance,1000)
# balance = withdraw(balance,2000)
# balance = withdraw(balance,500)
commission, balance = withdraw_night(balance,500)
print("수수료{0}원이며 , 잔액은 {1}원 입니다.".format(commission,balance))