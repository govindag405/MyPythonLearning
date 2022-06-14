class Car:
    def __init__(self,brand,make,model):
        self.brand=brand
        self.make=make
        self.model=model
    def milage(self):
        if self.brand == "Maruthi":
            print(f"Milage of {self.brand} is 21 km/hr")
        elif self.brand == "Hyundai":
            print(f"Milage of {self.brand} is 19 km/hr")
        elif self.brand == "Tata":
            print(f"Milage of {self.brand} is 20 km/hr")
        else:
            print(f"Don't go for {self.brand}")

car1 = Car("Maruthi",2022,"WagonR")
car1.milage()
car2 = Car("Hyundai",2022,"WagonR")
car2.milage()
car3 = Car("Tata",2022,"WagonR")
car3.milage()
car4 = Car("Ford",2022,"WagonR")
car4.milage()