try:
    input_1 = int(input("Please enter your first number: "))
    input_2 = int(input("Please enter your second number: "))

    result = input_1 / input_2
    print = 0  
    print(f"{input_1} divided by {input_2} is = {result}")
except ZeroDivisionError:
    print('Division by 0 is not possible')   

except ValueError:
    print("Invalid input provided")    