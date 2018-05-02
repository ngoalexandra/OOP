class Animal:
    def __init__(self, name = "", health= 100):
        self.health = health
        self.name = name
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health += 5
        return self
    def displayHealth(self):
        print('current health is:' +str(self.health))
        return self


class Dog(Animal):
    def __init__(self, health = 150, name = "barky"):
        super().__init__(name, health)
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self,health = 170, name = "turtle"):
        super().__init__()
    def fly(self):
        self.health -= 10
        return self
    def dragon_health(self):
        super().displayHealth()
        print("I'm a Dragon")
        return self


Animal().walk().walk().walk().run().run().displayHealth()
Dog().walk().walk().walk().run().run().pet().displayHealth()
Dragon().dragon_health()

Dog = Animal("spotty", 50)
print(Dog.name)
print(Dog.health)

dragon1 = Dragon(500,"bigred")
print(dragon1.health)

    



    
        
