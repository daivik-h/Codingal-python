class Parent:

    def __init__(self, eye_color, height):
        self.eye_color = eye_color
        self.height = height

    def show_traits(self):
        print(f"Eye color is {self.eye_color} an Height is {self.height}")   

class Child(Parent):

    def __init__(self, eye_color, height, name ,age, hobby):

        self.name = name
        self.age = age
        self.hobby = hobby
        super().__init__(eye_color, height)

    def show_traits(self):
        print(f"Name is {self.name} and age is {self.age}")
        super().show_traits() 
    def find_hobby(self):
        print(f"{self.hobby}")

obj_1 = Parent("brown", "162")
obj_2 = Child("blue", "170","Arun", "22", "Balet")
obj_1.show_traits()       
obj_2.show_traits()





        