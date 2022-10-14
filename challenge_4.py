




from calendar import c
from xml.dom.expatbuilder import InternalSubsetExtractor


class Account:

    def __init__(self,title,balance):
        self.title = title
        self.balance = balance

    
    def _title(self):
        print("Title:",self.title)
        print("Balance:",self.balance)
    
class Savingacc(Account):

    def __init__(self,title,balance,interest):
        super().__init__(title,balance)
        self.interest = interest

    def _interest(self):
        print("Rate:",self.interest)

obj = Savingacc("ashish",5000,5)
obj._title()
obj._interest()