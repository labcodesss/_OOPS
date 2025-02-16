#property decorator

class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        '''self.percentage=str((self.phy +self.chem +self.math)/3) +"%"


    def claculatePercentage(self):  
        self.percentage=str((self.phy +self.chem +self.math)/3) +"%"'''

    @property
    def percentage(self):
        return str((self.phy +self.chem +self.math)/3) +"%"

student1 =Student(97,98,99)
print(student1.percentage)   

student1.phy=88

print(student1.percentage)