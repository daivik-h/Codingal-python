buying_cost = float(input('Enter buying cost : '))
selling_cost = float(input('Enter selling cost : '))

loss = buying_cost - selling_cost
profit = selling_cost - buying_cost
if buying_cost > selling_cost:
    print(f'You lost your money {loss} dkk to be exact shame on you you dont know business')

elif buying_cost == selling_cost:  
    print ('You wasted your time on not getting a profit now you will not get a job as a seller')


else :
    print(f'Very good you made {profit} dkk you are a good business person')    