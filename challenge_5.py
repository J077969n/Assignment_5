


class account:
    def __init__(self,title=None,balance=0):
        self.title = input("enter your name:")
        self.balance = int(input("enter your account balance:"))


    def withdrawal(self,amount):
        self.balance -= amount

    def deposit(self,amount):
        self.balance += amount

    def get_balance(self):
        print("Account_ balance:",self.balance)
    
    

class saving_account(account):

    def __init__(self, title, balance,interest_rate):
        super().__init__(title, balance)
        self.interest_rate = interest_rate

    def interest_amount(self):
        interestamount = (self.interest_rate*self.balance)/100
        print("Interestamount:",interestamount)

account_obj = account("ashish",2000)
account_obj.withdrawal(int(input("enter the amount you want to withdraw:")))
account_obj.get_balance()
account_obj.deposit(int(input("enter the amount you want to deposit:")))
account_obj.get_balance()
saving_account_obj = saving_account("ashish",2000,5)
saving_account_obj.interest_amount()