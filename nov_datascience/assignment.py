import random
from datetime import datetime
def create_accno():
    num=16
    return random.randint((8*(num)-1),(10*(num-1)))

class BasicAccount:
    bank_name='SBI'

    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.mini_bal=2000
        self.acc_no=create_accno()
        self.card_no=None
        self.card_exp=None

    def deposit(self,depamount):
        self.depamount=depamount
        self.mini_bal+=self.depamount
        print('You have deposited:',depamount,
              'Your total balance is',self.mini_bal)

    def withdraw(self,withamount):
        self.withamount=withamount
        if withamount<self.mini_bal:
            self.mini_bal-=self.withamount
            print('You have withdrew:',withamount,'Your total balance is',self.mini_bal)
        else:
            print('Insufficient balance')

    def Balance(self):
        print(self.mini_bal)

    def Get_name(self):
        print(self.name)

    def Ava_bal(self):
        print('Your account number:',self.acc_no,'have',self.mini_bal)

    def Name(self):
        print(self.name)
    def NewCard(self):
        if self.card_no:
            print('Already issued')
        else:
            month=datetime.now().month
            year=str(datetime.now().year)
            year_int=int(year[2:])+3
            self.card_no=self.acc_no
            self.card_exp=(month,year_int)
            print('New card number:',self.card_no,'Exp date:',self.card_exp)

    def printvalues(self):
        print('Your',BasicAccount.bank_name,'with the account number:',self.acc_no,
              'has the balance:',self.mini_bal)

class PremiumAccount(BasicAccount):
    def __init__(self,acc_name,opening_bal,overdraft_amt):
        super().__init__(acc_name,opening_bal)
        self.overdraft=True
        self.overdraft_limit=overdraft_amt

    def __str__(self):
        return f'Premium{super().__str__()}Overdraft limit:{self.overdraft_limit}'

    def get_bal(self):
        return self.mini_bal-self.overdraft_limit
    def print_bal(self):
        print('Your account number:',self.acc_no,'Your total balance is:',self.mini_bal-self.overdraft_limit)

    def set_overdraft_limit(self,limit):
        self.overdraft_limit=limit
        return self.overdraft_limit

    def prm_withdraw(self,amount):
        self.amount=amount
        if self.amount<self.mini_bal+self.overdraft_limit:
            self.mini_bal-=self.amount
            print('Your',self.acc_no,'debited:',self.amount,
                  'Your total balance:',self.mini_bal+self.overdraft_limit)
        else:
            print('Insufficient Funds')

    def close_acc(self):
        if self.balance>0:
            print('Account closed')
            return True
        else:
            print('Cannot close account as coustmor is overdrawn by',self.get_bal())
            return False
customer1=BasicAccount('Sourav',1000)
customer1.printvalues()
print("-"*100)
customer1.NewCard()
print("-"*100)
customer1.deposit(3000)
print("-"*100)
customer1.withdraw(200)


print(""*100,"\n",""*100)

premium_customer=PremiumAccount('sourav',2000,500)
premium_customer.prm_withdraw(300)
print("-"*100)
premium_customer.print_bal()
print("-"*100)
premium_customer.close_acc()
