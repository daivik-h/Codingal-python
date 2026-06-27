user_input = int(input('Please enter a number and i will convert it into a Binary number(whole numebrs only): '))
binary = bin(user_input)
binaryremoved = binary[2:]
print(f'The Binary conversion of {user_input} is {binaryremoved}')