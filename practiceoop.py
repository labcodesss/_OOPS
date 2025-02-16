class Student:

    def __init__(self,name,marks): 
        self.name=name
        self.marks=marks
    
    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum=0  
        for val in self.marks:
            sum  += val
        print(f"hii {self.name} your score is {sum/3}")    

s1= Student ("tony",[99,98,97])   
s1.get_avg()     

s1.name="ironman"#objects can be manipulated in classes and objects
s1.get_avg()