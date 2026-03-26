result = 1
user_num = int(input('Enter a number: '))
to_the_power_of = int(input(f'Enter the power of the number: '))
result = 1
for i in range(to_the_power_of):
    result = result * user_num

print(f'{user_num} to the power of {to_the_power_of} is {result}')