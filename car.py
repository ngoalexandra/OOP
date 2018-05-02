class car:
    def __init__(self,original_price =0, max_speed = 0, fuel = 0, mileage = 0, tax = 0):
        self.price = original_price
        self.max_speed = max_speed
        self.fuel = fuel
        self.mileage = str(mileage) + 'mpg'
        self.tax = tax

        if (self.price > 10000):
            self.tax = 0.15
        else: 
            self.tax = 0.12

        if (self.fuel < 0.15):
            self.fuel = "empty"
        elif self.fuel > 0.15 and self.fuel < 0.50:
            self.fuel = "kinda fuel"
        elif self.fuel > 0.60:
            self.fuel = "full tank"

    def print_all(self):
        print(self.__dict__) 

Toyota = car(2000,105,0.50,28,0).print_all()
Audi = car(75000, 205,0.60,223).print_all()
car3 = car(2000,5,0.2,105).print_all()


# Toyota.__dict__ 
# returns all values in dict


