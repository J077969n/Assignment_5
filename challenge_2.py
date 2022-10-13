from __future__ import division
from audioop import add, mul


class calculater:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        addition = self.x + self.y
        print(addition)
    
    def subtract(self):
        subtractuon = self.x - self.y
        print(subtractuon)

    def multiply(self):
        mul = self.x*self.y
        print(mul)

    def divide(self):
        division = self.x/self.y
        print(division)

calculater_obj = calculater(10,94)
calculater_obj.add()
calculater_obj.subtract()
calculater_obj.multiply()
calculater_obj.divide()