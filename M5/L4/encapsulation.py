class Computer:
    __maxprice = 1000 

    def sell(self):
        print(f"The computer will be sold at ${self.__maxprice}")

    def apply_discount(self):
        self.__maxprice = 800
        print("The discount has been applied")

obj1 = Computer()
obj1.sell()
obj1.__maxprice = 700
obj1.sell()
obj1.apply_discount()
obj1.sell()