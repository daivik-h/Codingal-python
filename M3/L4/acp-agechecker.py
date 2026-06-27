try:
    age_user = int(input("Please enter your age: "))
    
    if age_user %2==0:
        print(f'{age_user} is an Even number and and it is also your age ')


    else:
        print(f'{age_user} is an odd number and is also your age  ')

except ValueError: 
    print("Invalid input provided")       