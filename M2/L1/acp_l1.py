age = int(input('Please enter your age: '))

if age > 13 and age < 50:
    print('Ok you can go for this ride')

elif age < 10 and age > 5 :
    parent = input('Are you with a parent (yes or no)')
    if parent =='yes':
        print('ok you can go')
    else:
        print('i am sorry you have to wait little one')    
    

else:
    print('Sorry you can not go for this ride')    