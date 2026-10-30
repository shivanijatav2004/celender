class Person:
    name = "anonymous"

    def changeName(self, name):
        self.name = name##changename ne new name de diya h self ki jgh person likhte h to return meranamee aayegaexmple
        self.__class__.name = name
       ## Person.name = name ##class variable ko change karne ke liye class ka naam lik

p1 = Person()
p1.changeName("shivani")   
print(p1.name)     
print(Person.name)

##class method
class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls, name):
        cls.name = name
       ## Person.name = name ##class variable ko change karne ke liye class ka naam lik
p1 = Person()
p1.changeName("shivani")   
print(p1.name)     
print(Person.name)
