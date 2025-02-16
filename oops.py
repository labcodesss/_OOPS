#types of case
'''
Pascal Case -> 
EmployeeName 

Camel Case->
isNumeric, isFloat
'''



'''class Number:
    def sum(self):
        return self.a +self.b
    
num =Number()#object instance
num.a=12
num.b=34
s= num.sum()
print(s)   
'''

'''class RailywayForm:#class
    formType="RailywayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

mounasApplication = RailywayForm()#object
mounasApplication.name="Mouna"
mounasApplication.train="Maharaja"
mounasApplication.printData()'''


#object attribute > class attribute

class Student:
    college_name="abc"#class attribute
    name="strange"

    def __init__(self):#default constructor
        pass

    def __init__(self, fullname,marks):#parameterised constructor
        self.name = fullname#object attribute
        self.marks = marks
        print("adding new student")


    def hello(self):
        print("welcome student", self.name)  

    def get_marks(self):
        return self.marks     
    

s1=Student("karan",97)   
#print(s1.name) 
s1.hello()
print(s1.get_marks())

'''s1=Student("karan",98)
print(s1.name,s1.marks)    

s2=Student("deepa",88)
print(s2.name,s2.marks)

print(Student.college_name)'''






'''class Car:
    color="blue"
    brand="bmw"
car1=Car()
print(car1.color)    
print(car1.brand) '''