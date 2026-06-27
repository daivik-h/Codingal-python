user_input = input('Enter A text to reverse: ') 

reverse = ""
for i in user_input:
    reverse = i + reverse
print(f'The Reversed Text is: {reverse}')    

if reverse == user_input:
    print('And it is a pallindrom')

else:
    print('But it is not a pallindrom')

