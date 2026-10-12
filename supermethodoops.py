class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")    
    @staticmethod
    def dtop():
        print("car stopped.")  
class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()
        

car1 = ToyotaCar("Prius", "elecctric")
print(car1.type)