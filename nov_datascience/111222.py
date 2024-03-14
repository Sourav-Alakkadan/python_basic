import random
from datetime import datetime

def create_ACnum():
    num=16
    return random.randint((8*(num)-1),(10*(num)-1))

class Basic_acc:
    bank='SBI'

    def _init_(self,name,balance):
        self.name=name
        self.balance=balance
        self.minimum_bal=1000
        self.acc_num=create_ACnum()
        self.card_num=None
        self.card_exp=None

    def Deposit(self,DepAmount):
        self.DepAmount=DepAmount
        self.minimum_bal+=self.DepAmount
        print("You Deposited:",DepAmount,"And Your balance is:",self.minimum_bal)

    def Withdraw(self,WAmount):
        self.WAmount=WAmount
        if WAmount<self.minimum_bal:
            self.minimum_bal-=self.WAmount
            print("You withdrew:",WAmount,"Your new Balance is:",self.minimum_bal)
        else:
            print("Insufficient Balance")

    def Balance(self):
        print(self.minimum_bal)

    def GetName(self):
        print(self.name)

    def AvailableBalance(self):
        print("You account number:",self.acc_num,"have:",self.minimum_bal," in your account")

    def Name(self):
        print(self.name)

    def NewCard(self):
        if self.card_num:
            print("Already issued")
        else:
            month=datetime.now().month
            year=str(datetime.now().year)
            year_int=int(year[2:])+3
            self.card_num=self.acc_num
            self.card_exp=(month, year_int)
            print("New card number:",self.card_num,"Exp date: ",self.card_exp)

    def printvalue(self):
        print("Your",Basic_acc.bank,"with the account number:",self.acc_num,
              "has the balance is:",self.minimum_bal)


class PremiumAccount(Basic_acc):
    def _init_(self,ac_name,opening_balance,overdraft_amt):
        super()._init_(ac_name,opening_balance)
        self.overdraft=True
        self.overdraft_limit=overdraft_amt

    def _str_(self):
        return f"Premium{super()._str_()},Overdraft limit:{self.overdraft_limit}"

    def get_balance(self):
        return self.minimum_bal-self.overdraft_limit

    def print_balance(self):
        print("Your account balance is:",self.balance-self.overdraft_limit)

    def set_overdraft_limit(self,limit):
        self.overdraft_limit=limit
        return self.overdraft_limit

    def prm_withdraw(self,amount):
        self.amount=amount
        if self.amount<self.balance+self.overdraft_limit:
            self.balance-=self.amount
            print("Your",self.acc_num, "debited:",self.amount,
                  "Your total balance is:",self.balance+self.overdraft_limit)
        else:
            print("Insufficient Funds")

    def close_account(self):
        if self.balance>0:
            print("Account closed")
            return True
        else:
            print("Cannot close account as customer is overdrawn by",self.get_balance())
            return False

# Example usage
customer1=Basic('v',1000)
customer1.printvalue()
print("-"*100)
customer1.NewCard()
print("-"*100)
customer1.Deposit(3000)
print("-"*100)
customer1.Withdraw(200)


print(""*100,"\n",""*100)

premium_customer=PremiumAccount('vis',2000,500)
premium_customer.prm_withdraw(300)
print("-"*100)
premium_customer.print_balance()
print("-"*100)
premium_customer.close_account()