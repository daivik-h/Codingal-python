print('The diomond pyramid (please enter the number of rows)')
n = int(input('here:'))
for i in range(n, 0, -1):
    for j in range(n - i):
        print(' ', end='')


    for k in range(i):
        print(' *', end='')      
    print()  