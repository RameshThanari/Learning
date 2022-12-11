class Car: #creating class
    attr1="Audi"
    attr2="Benz"
    attr3="Ferrai"

    def names(self): #creating Function
        print("The car name is",self.attr1)
        print("The car name is",self.attr2)
        print("The car name is",self.attr3)
MyCar = Car()  
print("my car is ",MyCar.attr1)
MyCar.names()     