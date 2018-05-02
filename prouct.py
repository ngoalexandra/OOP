class Product:
    def __init__(self,o_price = 0, item_name = 0, tax = 0, weight = 0, brand = 0, status = True):
        self.price = o_price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status
        if self.status == True:
            self.status = "For sale"
            print(self.status)
            
        else:
            self.status = "sold"
            print(self.status)
            
            
    def displayAll(self):
        print(self.__dict__)
    def sell(self):
        if self.status == False:
            self.status == "For Sale"
           
        elif self.status == True:
            self.staus == "Sold!!!!"
        print(self.status)
        return self

    def add_tax(self,tax = 0.12):
        self.price = round(self.price * (1+tax))
        return self

    def returning(self, reason_for_return):
        if reason_for_return == 1:
            self.reason_for_return == 'defective!!'
            self.price = 0
            self.status = false
            print(self.reason_for_return)
        else: 
            self.reason_for_return > 2
            self.reason_for_return == 'like new'
            self.status = True
            self.status = "for sale"
            print(self.reason_for_return)
            print(self.status)

        return self

    
product1 = Product(500, "iphone", 2, "apple")
print(product1.price)
product2 = Product(1000, "car", "2000")


            




    
