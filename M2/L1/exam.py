student_attedence = int(input('Please enter your attedence out of 100 : '))

if student_attedence < 75:
    cause = input('Do you have a medical cause (yes or no) : ')
    if cause == 'yes':
        print('OK you are allowd for this exam') 

    else:
        print('You are not allowd your parents will be informed see me at the principals office')



else :
    print('You are allowd for this exam')        