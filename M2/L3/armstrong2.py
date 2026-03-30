def is_armstrong(num):
    sum = 0
    temp = num
    
    while temp > 0:
        digit = temp%10
        sum += digit**len(str(num))
        temp //=10
    if sum == num:
        return True

    else:
        return False        

user_input = int(input('Enter Any Number And i whil check if it is a Armstrong Number:  '))

if is_armstrong(user_input):
    print(f'{user_input} is a Arnstrong number😱')        

else:
    print(f'Sorry {user_input} Is not a armstrong number 😏')            