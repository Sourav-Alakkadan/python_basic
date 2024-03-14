#Bank
#1 class
#acc details method1
#deposit method2
#withdrawal method3

class Bank:
    bank_name='SBI'
    def acc_details(self,fname,lname,accno):
        self.fname=fname
        self.lname=lname
        self.accno=accno
        self.minbalance=5000
        self.total=self.minbalance
    def deposit(self,cash):
        self.cash=cash
        self.total+=self.cash
        print('Your',Bank.bank_name,'acc has been credited',self.cash,'total balance',self.total)
    def withdraw(self,amount):
        self.amount=amount
        if self.total<self.amount:
            print('Insufficient Balance')
        else:
            self.total-=self.amount
            print('Your',Bank.bank_name,'acc has been debited',self.amount,'total balance',self.total)
per1=Bank()
per1.acc_details( 'vinay','k',54321)
per1.deposit(5000)
per1.withdraw(2000)
        
