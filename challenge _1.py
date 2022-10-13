



class  point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z 

    def sq_sum(self ):
        no1 = self.x**2
        no2 = self.y**2
        no3 = self.z**2
        print(f"{no1+no2+no3}")
    
        

point_obj = point(1,3,5)
point_obj.sq_sum()


