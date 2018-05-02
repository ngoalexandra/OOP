
class bike:
    def __init__(self, original_price = 0, max_speed = 0, miles = 0):
        self.price = original_price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print(self.price)
        print(self.max_speed)
        print(self.miles)
        return self
    def ride(self):
       self.miles += 10
       print("Ridin' Dirty")
       return self

    def reverse(self):
       print("backing up")
       self.price -=5 
       return self

bike1 = bike(0,0,0)
bike1.ride().ride().ride().reverse().displayInfo().ride()

bike2 = bike(56,3,20)
bike2.ride().reverse().reverse().displayInfo()

    

