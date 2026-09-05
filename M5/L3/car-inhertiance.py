class BaseCar:

    def __init__(self, brand,range ):
        self.brand = brand
        self.range = range

    def show_traits(self):
        print(f"Brand is {self.brand} an range is {self.range}")   

class NewModel(BaseCar):

    def __init__(self, brand, range, top_speed ,wheels, price):

        self.top_speed = top_speed
        self.wheels = wheels
        self.price = price
        super().__init__(brand, range)

    def show_traits(self):
        print(f"Top speed is {self.top_speed} and wheel size is {self.wheels}")
        super().show_traits() 
    def find_price(self):
        print(f"{self.price}")

obj_1 = BaseCar("Byd", "570km")
obj_2 = NewModel("Tesla", "600km","220km", "22in", "370,000dkk")
obj_1.show_traits()       
obj_2.show_traits()





        