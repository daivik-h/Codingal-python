starting_value = int(input("please enter your starting input (whole numbers only and starting value must be less than ending value): "))
ending_value = int(input("please enter your ending input (whole numbers only): "))
numbers = []

if starting_value >= ending_value:
    print('Did i not specifically write that the ending value greater than the starting value can you read or not are you alive are our parents proud of you or not!? ')
else:
    for i in range(starting_value, ending_value + 1 ):
        numbers.append(i)
    print(f"Your original list: {numbers}")
    size = len(numbers)
    print(f"The Size of the list is : {size}")
    sum = 0 
    for i in numbers:
        sum += i 
    print(f"Sum of the values in the list: {sum}")
    average = sum / size  
    print(f"The average of the list is: {average}")
    reversed_list = numbers [:: -1]
    print(f"The list reversed is: {reversed_list}")
    print(f"Your original list stays intact: {numbers}")