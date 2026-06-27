def needs_more(need_pay,payed):
    return need_pay - payed
def return_bak(need_pay,payed):
    return payed - need_pay
need_pay = float(input("Hey how much do you need to pay: "))
payed = float(input("Ok How Much Did You Pay: "))

if need_pay > payed:
    print(f'Ok you still need to pay {needs_more (need_pay,payed)}')

elif need_pay < payed:
    print(f'Ok the shop keeper need to give back {return_bak (need_pay,payed)}')
elif need_pay == payed:
    print("You have payed all the amount")    

else:
    print("Invalid input")
