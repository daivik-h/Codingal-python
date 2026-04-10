def add(value_1,value_2):
    return value_1 + value_2 
def sub(value_1,value_2):
    return value_1 - value_2 
def mul(value_1,value_2):
    return value_1 * value_2 
def div(value_1,value_2):
    return value_1 / value_2 

value_1 = float(input("Please enter a number: "))
value_2 = float(input("Plase enter a second number: "))
print(f'Your first value is {value_1}')
print(f'Your second value is {value_2}')
print("Plase enter an oprator of your choice \n1.Add\n2.Subtract\n3.multiply\n4.Divide\n(Please enter in number 1-4 NO SPACE)")
oprator_choice = input("Go Ahead Here: ")
if oprator_choice == "1":
    print(f'The Addition of {value_1} and {value_2} is {add(value_1,value_2)}')
elif oprator_choice == "2":
    print(f'The Subtraction of {value_1} and {value_2} is {sub(value_1,value_2)}')
elif oprator_choice == "3":
    print(f'The Multiplication of {value_1} and {value_2} is {mul(value_1,value_2)}')
elif oprator_choice == "4":
    print(f'The Division of {value_1} and {value_2} is {div(value_1,value_2)}')

else:
    print('Did you not hear my you little brat i told you no space and only values from 1-4 can you even read i would not be suprised if your parents werent proud of you are you even proud of yourself go back to school or get some glasses!!!!')    
            
