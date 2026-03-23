starting_value = int(input('Enter a starting number:'))
ending_value = int(input('Enter the ending: ')) 

if starting_value >= ending_value:
    print('Are you dumb i specifically wrote that you should do the starting value first do you have a mental sickness if you have i am sorry but if not yuo should be having it !')
else: 
    for i in range(starting_value,ending_value + 1):
        if i % 2 == 0:
            print(i)