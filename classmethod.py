'''class Person:
    name="Stranger"

    def changeName(self,name):
        #Person.name=name--> one of the method to change the name in the class
        self.__class__.name="rahul"
    

    @classmethod
    def changeName(cls, name):
        cls.name=name
        
p1 = Person()
p1.changeName("rahul kumar")
print(p1.name) 
print(Person.name)     '''  


#property decorator

class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percentage=str((self.phy +self.chem +self.math)/3) +"%"


    def claculatePercentage(self):  
        self.percentage=str((self.phy +self.chem +self.math)/3) +"%"

student1 =Student(97,98,99)
print(student1.percentage)   

student1.phy=88
print(student1.phy)
student1.claculatePercentage()
print(student1.percentage)