user_input = int(input('Enter any number and i will find the sum from 1 till that number (Natural Numbers Only): '))

sum = 0
i = 1 
while i <= user_input:
    sum += i
    i += 1

print(f'This is your answer {sum}')    