country_code = {'India': '0091','Australia': '0025','Nepal': '00977','Denmark': '0045','USA':'001','Brazil': '0055'}

country_input = input("please enter the name of your country (India,Australia,Nepal,Denmark,USA,Brazil): ")

for country in country_code:
    if country == country_input:
        print(country_code[country])
