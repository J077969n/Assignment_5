



class student:
    

        
    
    def  set_Name(self,name):
        self.__name = name

    def  get_Name(self):
        return self.__name

    def  set_Rno(self,rno):
        self.__Rno = rno
    
    def  display(self):
        print("Name:",self.__name)
        print("Rno:",self.__Rno)

obj = student()
obj.set_Name("nikhil")
obj.set_Rno(85)
obj.display()