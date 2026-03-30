def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True    

user_input = int(input('Enter a number and i will check if it is prime: '))
if is_prime(user_input):
    print(f'{user_input} is a prime number ')
else:
    print(f'{user_input} is not a prime number')    