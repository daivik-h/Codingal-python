print('The diomond pyramid (please enter the number of rows)')
n = int(input('here:'))
for i in range(n):
    for j in range(n - 1 - i):
        print(' ',end='')



    for k in range(i + 1):
        print(' *', end='')      

    print()    
for i in range(n, 0, -1):
    for j in range(n - i):
        print(' ', end='')


    for k in range(i):
        print(' *', end='')      
    print()    
    
