print('The inverted pyramid (please enter the number of rows)')
n = int(input('here:'))
space_between = n - 1
for i in range(n):
    for j in range(n - 1 - i):
        print(' ',end='')



    for k in range(i+1):
        print('*', end='')      

    print()    