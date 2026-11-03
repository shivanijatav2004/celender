class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
       # self.percentage = (phy + chem + math) / 3
    
    #percentage ko change krne ke liye method bna diya
    def calculatePercentage(self):
       self.percentage = str((self.phy +self. chem +self.math) / 3) + "%"

    ##propery mehtod
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

  
stu1 = Student(98, 97, 99)  
print(stu1.percentage)      
stu1.phy = 86
# stu1.calculatePercentage()
print(stu1.percentage)  ##percentage change nhi hoga kyuki percentage ko humne init me hi define kr diya h