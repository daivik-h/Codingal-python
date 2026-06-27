print('The diomond pyramid (please enter the number of rows)')
n = int(input('here:'))
number = 1 
for i in range(n): 
    for j in range(i+1):
    
        print(f'{number} ', end="")
        number += 1
    print()