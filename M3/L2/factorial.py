def find_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * find_factorial(n-1) 

number_user = int(input('Please enter any whole numeber and i will say the factorial of it : '))
print(f'The factorial of {number_user} is {find_factorial (number_user)}')
