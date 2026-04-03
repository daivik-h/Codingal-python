deci_input = int(input('Please enter a number and i will convert it into a Binary number(whole numebrs only): '))
binary = bin(deci_input)
binaryremoved = binary[2:]
print(f'The Binary conversion of {deci_input} is {binaryremoved}')