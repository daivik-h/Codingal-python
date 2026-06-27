user_input = input('Enter A word : ')
print(f'Data Type of Your Input Is : {type(user_input)}')

reversed = user_input[::-1]

print(f'ReversedValue Is = {reversed}')

if reversed == user_input :
 print('Ohh Your Input Is a Pallindrom Wuhoo')

else: 
 print('Ohh Noo Your Input Is Not A pallinDrom womp Womp Womp')
