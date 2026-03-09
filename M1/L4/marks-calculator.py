name = input('Enter Your Name: ')
grade = input('Enter Your Grade: ')


print(f'Hello {name} , you are in grade {grade}, nice to meet you ,fill out this form. ')

maths_marks = float(input('Enter Your Marks For Maths (max is 25)     : '))
english_marks = float(input('Enter Your Marks For English (max is 25) : '))
history_marks = float(input('Enter Your Marks For History (max is 25) : '))
coding_marks = float(input('Enter Your Marks For Coding (max is 25)   : '))

full_marks = 100
total_marks = maths_marks + english_marks + history_marks + coding_marks

average_marks = total_marks / 4

percentage_marks = total_marks / full_marks * 100 

print(f'Ok {name} your total marks in all subjects is {total_marks} out of {full_marks} so your average marks per subjet is {average_marks} and you got {percentage_marks}% in this test.' )


if percentage_marks >= 70:
    print(f'Congratulations {name} You Have Passed.')

else :
    print(f'Congratulations {name} YOU HAVE FAILED YOUR PARENTS AND THIS TEST !!! .')


