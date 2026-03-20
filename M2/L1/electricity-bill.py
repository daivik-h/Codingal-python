unit = float(input('Please enter the number of units you have consumed in the past month :  '))

total = 0
maintancecharge = 0
increment = 0 
if unit < 50 :
    total = unit * 2.6 + 25
elif unit > 50 and unit < 100:
    total = (unit * 2.6 + 25) * 1.05

elif unit > 100 and unit < 200:
    total = (unit * 2.6 + 25) * 1.10

else :
    total = (unit * 2.6 + 25) * 1.15   


print(f'Your Units for this month is {unit} that brings you total to ${total} inklusive VAT150')     
