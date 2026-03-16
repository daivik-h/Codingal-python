temperature = int(input('Hey Enter The Temerature : '))
 


if temperature < 0:
    print(f'The Temperature is {temperature} thats frezing you better take a good sweater or hoddie and remember the basse layer and jacket 🥶')

elif temperature > 0 and temperature <= 10 :
    print(f'The Temperature is {temperature} stil pretty cold you better take a good sweater or hoddie and remember a coat 🤧 ')   

elif temperature > 10 and temperature <= 16 :
    print(f'The Temperature is {temperature} thats perfect a shirt with a pull over should be fine 😊')    

elif temperature > 16  :
    print(f'The Temperature is {temperature} thats thats perfect summer temperature take a tshirt and shorts or pant is fine you will sweat anyway 😁😎🥵') 

else :
    print('invalid temparature')       
