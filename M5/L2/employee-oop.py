class Employee: 
    def __init__(self,designation,city,salary):
        self.designation = designation
        self.city = city
        self.salary = salary
        print("New Employee created")
    def __del__(self):
        print("Destructor called ")  

e1 = Employee("Hardware engineer","London","50,000")         