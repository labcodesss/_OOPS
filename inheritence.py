#single inheritance 
class Car:
    def __init__(self,type):
         self.type=type


    @staticmethod
    def start():
        print("Car started")

    @staticmethod  
    def stop():
        print("stop car")  

class Toyota(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)
        super().start()

#Multilevel inheritance
'''class Fortuner(Toyota):
     def __init(self,type):
         self.type =type   '''  


car1= Toyota("prius","electrical")
print(car1.type)



'''class A:
    varA="welcome to class A"

class B:
    varB = "welcome to class B"    

class C(A,B):
     varC = "welcome to class C"  


c1 = C()
 
print(c1.varC)
print(c1.varB)
print(c1.varA)'''

