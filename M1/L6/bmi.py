height = float(input('Enter Your Height in meters : ')) 
weight = float(input('Enter Your Weight in Kg : '))

bmi = weight / height ** 2 

if bmi < 18.5 :
    print(f'Your BMI i {bmi} Eat something man !!! you are under weight')

elif bmi >= 18.5 and bmi < 25 :
    print(f'Your BMI is {bmi} you are perfectly normal weight') 

elif bmi >= 25 and bmi < 30 :
    print(f'Your BMI {bmi} get youself together and exericise a bit more than usual you are over weight ')    

elif bmi >= 30 and bmi < 35 :
    print(f'Your BMI {bmi} what are you doing i guees you are siting in your room and eating fat person you are in Obesity class 1 this  is a significant health concern that increases the risk of mortality and chronic diseases get yourself together !!!! ')     

elif bmi >= 35 and bmi < 40 :
    print(f'Your BMI {bmi} what are you doing i guees you are siting in your room and eating more than you brun big fat person you are in Obesity class 2 this  is considered a moderate-to-high risk condition that significantly increases the likelihood of developing severe comorbidities, including type 2 diabetes, heart disease, hypertension, and sleep apnea get yourself together !!!!! ')    

elif bmi >= 40  :
    print(f'Your BMI {bmi} you are so fat that when you walk the earthquak siren starts makes sense since you are in obesity class 3 this is also highly dangerous, significantly increasing the risk of premature death, potentially shortening life expectancy by up to 14 years. i think you need to exercise (A lot fat person )  !!!!!! ')     


else :
    print('Invalid input')       