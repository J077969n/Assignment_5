


from ssl import ALERT_DESCRIPTION_HANDSHAKE_FAILURE
from turtle import title


class Account:

    def __init__(self):
        print("ashish")
        print(5000)
    
    def _title(self):
        print("ashish")
        print(5000)
    
class SavingAC(Account):
    def __init__(self):
        super().__init__()
        print(5)


obj = SavingAC()
