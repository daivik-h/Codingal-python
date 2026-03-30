user_num = input('Enter a number(greater than 4): ')
if  len(user_num) > 4:
    midindex = (len(user_num) -1)//2
    first = int(user_num[midindex])
    second = int(user_num[midindex +1])

    print(f'The product of the middle digits is {first * second}')
else:
    
    print('The input is to low')